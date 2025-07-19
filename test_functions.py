# test_all_functions.py

from src.weather import get_weather
from src.crop_recommender import recommend_crop
from src.pest_disease import detect_pest_or_disease
from src.irrigation import get_irrigation_advice
from src.fertilizer_advisor import advise_fertilizer
from src.yield_predictor import predict_yield
from src.auth import (
    create_user_table, add_user, login_user,
    get_user_question, verify_answer, update_password,
    hash_password
)

print("\n✅ TESTING ALL MODULES OF AGROMIND")

# 1. Weather
print("\n🌤️ Weather:")
weather = get_weather("Delhi")
if weather:
    print(f"  Temp: {weather['temperature']}°C, Humidity: {weather['humidity']}%, Description: {weather['description']}")
else:
    print("  ❌ Failed to fetch weather (check API key or internet).")

# 2. Crop Recommender
print("\n🌾 Crop Recommender:")
try:
    crop = recommend_crop(90, 40, 40, 30, 70, 6.5, 200)
    print(f"  ✅ Recommended Crop: {crop}")
except Exception as e:
    print(f"  ❌ Error: {e}")

# 3. Pest / Disease
print("\n🐛 Pest & Disease Detection:")
symptoms = ["leaf spot on leaves", "wilting of stems", "some unknown issue"]
for s in symptoms:
    print(f"  Symptom: '{s}' → {detect_pest_or_disease(s)}")

# 4. Irrigation Advice
print("\n💧 Irrigation Advice:")
print(f"  Advice (38°C, 25% humidity, 20mm rain): {get_irrigation_advice(38, 25, 20)}")
print(f"  Advice (30°C, 50% humidity, 120mm rain): {get_irrigation_advice(30, 50, 120)}")

# 5. Fertilizer Advisor
print("\n🧪 Fertilizer Advice:")
try:
    advice = advise_fertilizer("rice", 80, 40, 40)
    print(f"  ✅ {advice}")
except Exception as e:
    print(f"  ❌ Error: {e}")

# 6. Yield Predictor
print("\n📊 Yield Predictor:")
try:
    yield_prediction = predict_yield("rice", 100, 90, 30, 75, 6.8, 250)
    print(f"  ✅ Predicted Yield: {yield_prediction} quintals/hectare")
except Exception as e:
    print(f"  ❌ Error: {e}")

# 7. Auth System
print("\n🔐 Auth System:")
create_user_table()

username = "testuser"
password = "test123"
hashed_pw = hash_password(password)
question = "Your favorite color?"
answer = "blue"

# Sign Up
if add_user(username, hashed_pw, question, answer):
    print("  ✅ User registered.")
else:
    print("  ⚠️ User already exists.")

# Login
if login_user(username, hashed_pw):
    print("  ✅ Login successful.")
else:
    print("  ❌ Login failed.")

# Security Question
q = get_user_question(username)
print(f"  🔎 Security Question: {q}")

# Verify Answer
if verify_answer(username, answer):
    print("  ✅ Answer verified.")
else:
    print("  ❌ Wrong answer.")

# Password Reset
new_pass = "newpass123"
if update_password(username, hash_password(new_pass)):
    print("  🔁 Password updated.")
else:
    print("  ❌ Failed to update password.")

# 8. Chatbot
print("\n💬 Chatbot Response Test:")
try:
    from src.chatbot import get_bot_response

    queries = [
        "Hello!",
        "I need fertilizer suggestion",
        "What's the weather in my farm?",
    ]

    for q in queries:
        response = get_bot_response(q)
        print(f"  👤 You: {q}\n  🤖 Bot: {response}")

except ImportError:
    print("  ⚠️ Chatbot module not found or function missing.")
except Exception as e:
    print(f"  ❌ Error in chatbot test: {e}")
