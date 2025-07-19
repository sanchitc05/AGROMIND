# Pest and disease detection logic
def detect_pest_or_disease(symptom):
    if "leaf spot" in symptom.lower():
        return "Possible fungal infection. Use Mancozeb spray."
    elif "wilting" in symptom.lower():
        return "Could be bacterial wilt. Remove infected plants."
    else:
        return "Unknown condition. Consult agriculture expert."