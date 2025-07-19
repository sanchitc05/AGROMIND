# Irrigation scheduling logic
def get_irrigation_advice(temp, humidity, rainfall):
    if rainfall > 100:
        return "No irrigation needed. Rainfall is sufficient."
    elif humidity < 30 and temp > 35:
        return "Irrigate twice a week."
    else:
        return "Irrigate once a week."
