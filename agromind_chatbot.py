# chatbot.py

def chat_response(query):
    query = query.lower()

    # Basic keyword-based replies
    responses = {
        "how to grow rice": "Rice needs plenty of water, high humidity, and loamy soil. Ideal temperature: 20°C–30°C.",
        "fertilizer for banana": "Banana plants need nitrogen, phosphorus, and potassium-rich fertilizer every 2 months.",
        "ideal temperature for mango": "Mango trees grow best at temperatures between 24°C and 30°C.",
        "best soil for wheat": "Wheat grows best in well-drained loamy or clay loam soils.",
        "coffee conditions": "Coffee thrives in humid, tropical climates with shade and high elevation.",
        "pH for tomato": "Tomatoes prefer slightly acidic soil with pH 6.0 to 6.8.",
        "rainfall for jute": "Jute needs about 150–200 cm of rainfall and a warm, humid climate.",
        "coconut tree care": "Coconut trees need sandy soil, high humidity, and regular watering.",
        "grape farming tips": "Grapes need good sun exposure, dry climate, and pruning for best yield.",
        "hii": "hello how can i help you"
    }

    for key, answer in responses.items():
        if key in query:
            return answer

    # Default fallback
    return "Sorry, I don't have an answer for that yet. Please consult a local expert or extension officer."
