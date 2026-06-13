import google.generativeai as genai
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
from gtts import gTTS

# =========================
# Gemini Setup
# =========================

API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# Page Setup
# =========================

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌱",
    layout="wide"
)

# =========================
# Language Selection
# =========================

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Telugu", "Hindi"]
)

# Voice Language Mapping

voice_lang = "en"

if language == "Telugu":
    voice_lang = "te"

elif language == "Hindi":
    voice_lang = "hi"

# =========================
# Title
# =========================

st.title("🌱 AgriVision AI")

st.subheader(
    "Smart Crop Disease Detection & Farmer Advisory System"
)

st.write(
    "AI-powered agriculture assistant using Google Gemini AI."
)

# =========================
# Crop Disease Detection
# =========================

st.header("📷 Crop Disease Detection")

image = st.file_uploader(
    "Upload Crop Image",
    type=["jpg", "jpeg", "png"]
)

if image:

    st.image(image, width=400)

    if st.button("Analyze Crop"):

        with st.spinner("Analyzing Crop..."):

            try:

                img = Image.open(image)

                prompt = f"""
                You are an agriculture expert.

                Answer ONLY in {language} language.

                Analyze this crop image and provide:

                1. Disease Name
                2. Symptoms
                3. Causes
                4. Treatment
                5. Prevention
                6. Confidence Percentage
                7. Limitations
                """

                response = model.generate_content(
                    [prompt, img]
                )

                st.success("Analysis Complete")

                st.write(response.text)

                # Audio

                tts = gTTS(
                    text=response.text[:1000],
                    lang=voice_lang
                )

                tts.save("crop_response.mp3")

                with open(
                    "crop_response.mp3",
                    "rb"
                ) as audio_file:

                    st.audio(
                        audio_file.read(),
                        format="audio/mp3"
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

# =========================
# AI Farmer Assistant
# =========================

st.divider()

st.header("🤖 AI Farmer Assistant")

question = st.text_input(
    "Ask a farming question"
)

if st.button("Ask AI"):

    if question:

        try:

            prompt = f"""
            You are an agriculture expert.

            Answer ONLY in {language} language.

            Question:
            {question}
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

            # Audio

            tts = gTTS(
                text=response.text[:1000],
                lang=voice_lang
            )

            tts.save("chat_response.mp3")

            with open(
                "chat_response.mp3",
                "rb"
            ) as audio_file:

                st.audio(
                    audio_file.read(),
                    format="audio/mp3"
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# =========================
# Weather Advisor
# =========================

st.divider()

st.header("🌦️ Weather Advisor")

city = st.text_input(
    "Enter City Name"
)

if st.button("Get Weather Advice"):

    if city:

        try:

            prompt = f"""
            You are an agriculture and weather expert.

            Provide farming guidance for farmers in {city}.

            Include:

            1. Weather Outlook
            2. Irrigation Advice
            3. Crop Protection Tips
            4. Farming Recommendations

            Answer ONLY in {language}.
            """

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

            # Audio

            tts = gTTS(
                text=response.text[:1000],
                lang=voice_lang
            )

            tts.save("weather_response.mp3")

            with open(
                "weather_response.mp3",
                "rb"
            ) as audio_file:

                st.audio(
                    audio_file.read(),
                    format="audio/mp3"
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# =========================
# Model Information
# =========================

st.divider()

st.header("📘 Model Information")

st.write("""
**Model Used:** Gemini 2.5 Flash

**API Used:** Google Gemini API

**Features**
- Crop Disease Detection
- AI Farmer Assistant
- Weather Advisor
- Multi-language Support
- Audio Responses
- Mobile Friendly Interface
""")

# =========================
# Disclaimer
# =========================

st.divider()

st.header("⚠️ Disclaimer")

st.warning(
    "This application provides AI-generated agricultural advice. Please consult agricultural experts before making critical farming decisions."
)