from src.weather import get_weather

api_key = "your_openweather_api_key"
city = "Delhi"
result = get_weather(api_key, city)
print(result)
