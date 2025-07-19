# weather.py
import requests

def get_weather(city):
    api_key = "49b2d220d623b02960de7b7615450a61"  # Replace with your actual key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "weather": data["weather"][0]["main"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
        return weather
    else:
        raise Exception(f"Error fetching weather: {response.status_code} - {response.text}")
