# python -m streamlit run "app.py"
import streamlit as st
import requests
from auth import *
from crop_recommender import recommend_crop
from india_locations import indian_locations
from models import fertilizers
from models import irrigation
from models import pest_disease
from voice_bot import run_voice_chat  # ✅ Corrected import for voice chatbot
from PIL import Image
import os

def chat_response(query):
    query = query.lower()

    responses = {
        "how to grow rice": "Rice needs a lot of water, high humidity, and loamy soil.",
        "best fertilizer for wheat": "Use nitrogen-rich fertilizer like urea for wheat.",
        "ph for tomato": "Tomatoes prefer slightly acidic soil with pH between 6.0 to 6.8.",
        "ideal temperature for mango": "Mango trees grow best between 24°C and 30°C.",
        "banana care": "Bananas need lots of water and potassium fertilizer.",
        "soil for cotton": "Black soil or well-drained loamy soil is best for cotton.",
        "coffee conditions": "Coffee grows well in tropical, shaded areas with high rainfall.",
        "when to grow maize": "Maize is best grown in warm weather from June to August.",
        "rainfall needed for jute": "Jute needs around 150–200 cm of rainfall.",
        "what to grow in july": "In July, rice, maize, soybean, and cotton are good choices.",
        "how to protect crops from pests": "Use neem spray or certified bio-pesticides regularly.",
        "grapes climate": "Grapes prefer dry and warm weather with less rainfall.",
        "urvarak kya de": "Fasal ke liye NPK ya compost de sakte hain.",
        "beej kaise chune": "Certified aur disease-free beej chunein.",
        "watermelon farming": "Watermelons need sandy loam soil and warm climate.",
        "coconut tree care": "Coconut trees prefer coastal sandy soil and regular watering.",
        "blackgram soil": "Loamy to clayey soil is best for blackgram.",
        "lentil temperature": "Lentils grow in cool climate and need loamy soil.",
        "pomegranate care": "Dry climate and less rainfall is good for pomegranates.",
        "cotton fertilizer": "Cotton needs nitrogen, phosphorus, and potassium.",
        "mango fertilizer": "Apply NPK and compost twice a year for mango trees.",
        "kya ugaye": "Kripya apni mitti aur mausam ki jankari dein.",
        "hii": "Hello! How can I help you with your farming needs?",
        "namaste": "Namaste! Aap kya jaanna chahenge krishi ke baare mein?"
    }

    for key, answer in responses.items():
        if key in query:
            return answer

    return "क्षमा करें, मेरे पास अभी तक इसका जवाब नहीं है। कृपया एक स्थानीय विशेषज्ञ या विस्तार अधिकारी से परामर्श करें।"

create_user_table()
st.set_page_config(page_title="AgroMind", page_icon="🌿", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

menu = ["Login", "Sign Up", "Forgot Password"]
choice = st.sidebar.selectbox("👤 Account", menu)

if choice == "Login":
    st.title("🔐 Login to AgroMind")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, hash_password(password)):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid credentials.")

elif choice == "Sign Up":
    st.title("📝 Create Account")
    new_user = st.text_input("Choose a Username")
    new_pass = st.text_input("Choose a Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")
    question = st.text_input("Security Question")
    answer = st.text_input("Answer")
    if st.button("Register"):
        if new_pass != confirm_pass:
            st.warning("Passwords do not match.")
        elif not new_user or not new_pass or not question or not answer:
            st.warning("Fill all fields.")
        else:
            if add_user(new_user, hash_password(new_pass), question, answer):
                st.success("Account created! Please login.")
            else:
                st.error("Username already exists.")

elif choice == "Forgot Password":
    st.title("🔑 Password Recovery")
    user = st.text_input("Enter your username")
    if user:
        question = get_user_question(user)
        if question:
            st.info(f"Security Question: {question}")
            ans = st.text_input("Answer")
            if st.button("Verify"):
                if verify_answer(user, ans):
                    new_pass = st.text_input("New Password", type="password")
                    confirm_pass = st.text_input("Confirm Password", type="password")
                    if st.button("Reset Password"):
                        if new_pass == confirm_pass:
                            update_password(user, hash_password(new_pass))
                            st.success("Password reset successfully.")
                        else:
                            st.warning("Passwords do not match.")
                else:
                    st.error("Incorrect answer.")
        else:
            st.error("User not found.")

if st.session_state.logged_in:
    st.sidebar.success(f"Logged in as: {st.session_state.username}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.markdown(
        "<h1 style='text-align: center; color: #2e7d32;'>🌱 AgroMind - Smart Crop Assistant</h1>",
        unsafe_allow_html=True
    )

    st.subheader("📍 Location & Weather")
    state = st.selectbox("Select State", sorted(indian_locations.keys()))
    city = st.selectbox("Select City", sorted(indian_locations[state]))
    st.success(f"Location Selected: {city}, {state}")

    api_key = "fa393f254109f8c31396e98d44c9228d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    default_temp, default_humidity = 25.0, 60
    try:
        response = requests.get(url)
        weather_data = response.json()
        weather_main = weather_data["weather"][0]["main"]
        default_temp = weather_data["main"]["temp"]
        default_humidity = weather_data["main"]["humidity"]
        st.info(f"🌡️ Temperature: {default_temp}°C  |  💧 Humidity: {default_humidity}%  |  ☁️ Weather: {weather_main}")
    except:
        st.warning("Weather data unavailable. Using default values.")

    st.subheader("🌿 Recommend the Best Crop")
    soil_type = st.selectbox("Select Soil Type", ["Loamy", "Sandy", "Clayey", "Silty", "Peaty", "Chalky"])

    soil_defaults = {
        "Loamy": (80, 60, 40), "Sandy": (50, 30, 20), "Clayey": (70, 60, 50),
        "Silty": (65, 55, 40), "Peaty": (75, 45, 40), "Chalky": (60, 40, 35),
    }
    soil_ph_defaults = {
        "Loamy": 6.8, "Sandy": 6.2, "Clayey": 7.0,
        "Silty": 6.5, "Peaty": 5.5, "Chalky": 7.5
    }
    rainfall_defaults = {
        "Loamy": 150, "Sandy": 60, "Clayey": 120,
        "Silty": 100, "Peaty": 200, "Chalky": 90
    }

    default_N, default_P, default_K = soil_defaults[soil_type]
    default_ph = soil_ph_defaults[soil_type]
    default_rainfall = rainfall_defaults[soil_type]

    with st.expander("⚙️ Customize Soil & Weather Inputs"):
        col1, col2, col3 = st.columns(3)
        with col1:
            N = st.slider("🟢 Nitrogen (N)", 0, 140, value=default_N)
        with col2:
            P = st.slider("🔵 Phosphorous (P)", 0, 140, value=default_P)
        with col3:
            K = st.slider("🔠 Potassium (K)", 0, 200, value=default_K)

        col4, col5, col6 = st.columns(3)
        with col4:
            temp = st.slider("🌡️ Temperature (°C)", 10.0, 50.0, value=default_temp)
        with col5:
            humidity = st.slider("💧 Humidity (%)", 10, 100, value=default_humidity)
        with col6:
            ph = st.slider("🌱 Soil pH", 3.5, 9.0, value=default_ph)

        col7, _, _ = st.columns(3)
        with col7:
            rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, value=default_rainfall)

    if st.button("🚀 Recommend crop"):
        crop = recommend_crop(N, P, K, temp, humidity, ph, rainfall)
        st.success(f"Recommended Crop: 🌾 **{crop.upper()}**")

        # 🔽 Show crop image if available
        image_path = f"images/{crop.lower()}.jpg"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            st.image(img, caption=f"{crop.upper()} Crop", width=700)
        else:
            st.warning("🔍 Image not found for the recommended crop.")

    st.subheader("🧪 Fertilizer Recommendation")
    if st.button("🧪 Recommend Fertilizer"):
        advice = fertilizers.recommend_fertilizer(N, P, K)
        st.info(advice)

    st.subheader("🚿 Irrigation Advice")
    if st.button("💧 Get Irrigation Advice"):
        tip = irrigation.get_irrigation_advice(temp, humidity, rainfall)
        st.success(tip)

    st.subheader("🐛 Pest & Disease Diagnosis")
    user_symptom = st.text_input("Describe symptoms (e.g., leaf spot, wilting):")
    if st.button("🦠 Diagnose"):
        if user_symptom:
            result = pest_disease.detect_pest_or_disease(user_symptom)
            st.warning(result)

    st.subheader("🧠 Ask AgroBot")
    user_query = st.text_input("Type your question...")
    if st.button("💬 Ask"):
        if user_query:
            reply = chat_response(user_query)
            st.session_state.chat_history.append(("You", user_query))
            st.session_state.chat_history.append(("AgroBot", reply))

    for speaker, text in reversed(st.session_state.chat_history[-6:]):
        st.markdown(f"**{speaker}:** {text}")

    st.subheader("🎧 Voice Chatbot in Local Language")
    run_voice_chat(state)
