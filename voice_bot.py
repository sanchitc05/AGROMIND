# agromind_voicebot.py
try:
    import streamlit as st
except ModuleNotFoundError:
    print("streamlit module is not installed. Please install it using 'pip install streamlit'")
    raise

try:
    import speech_recognition as sr
except ModuleNotFoundError:
    print("speech_recognition module is not installed. Please install it using 'pip install SpeechRecognition'")
    raise

from gtts import gTTS
from langdetect import detect
from deep_translator import GoogleTranslator
import os
import time
from agromind_chatbot import chat_response

# Optional: language map based on state
language_map = {
    "Punjab": "pa",
    "Haryana": "hi",
    "Rajasthan": "hi",
    "Uttar Pradesh": "hi",
    "Madhya Pradesh": "hi",
    "Bihar": "hi",
    "Delhi": "hi",
    "Maharashtra": "mr",
    "Gujarat": "gu",
    "West Bengal": "bn",
    "Tamil Nadu": "ta",
    "Kerala": "ml",
    "Karnataka": "kn",
    "Andhra Pradesh": "te",
    "Telangana": "te",
    "Odisha": "or",
    "Assam": "as",
    "Manipur": "mni",
    "Nagaland": "en",
    "Mizoram": "en",
    "Arunachal Pradesh": "en",
    "Sikkim": "ne",
    "Jharkhand": "hi",
    "Chhattisgarh": "hi",
    "Tripura": "bn"
    # Add more as needed
}

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except:
        return "Sorry, I couldn't understand your voice."

def translate_text(text, target_lang='hi'):
    try:
        detected = detect(text)
        translated = GoogleTranslator(source=detected, target=target_lang).translate(text)
        return translated
    except:
        return text

def speak_text(text, lang='hi'):
    tts = gTTS(text=text, lang=lang)
    filename = f"temp_{int(time.time())}.mp3"
    tts.save(filename)
    st.audio(filename, format="audio/mp3")
    return filename

def run_voice_chat(state):
    st.header("🗣️ Voice Chatbot (Local Language Support)")
    if st.button("🎙️ Start Talking"):
        spoken_text = listen_microphone()
        st.success(f"You said: {spoken_text}")

        local_lang = language_map.get(state, "hi")

        translated_to_english = translate_text(spoken_text, "en")
        bot_reply_en = chat_response(translated_to_english)
        bot_reply_local = translate_text(bot_reply_en, local_lang)

        st.info(f"🤖 AgroBot says (in {local_lang}): {bot_reply_local}")
        audio_file = speak_text(bot_reply_local, lang=local_lang)

        # Cleanup
        if os.path.exists(audio_file):
            os.remove(audio_file)
