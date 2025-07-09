from api.openweathermap import fetch_weather
from utils.display import print_weather

class WeatherDashboard:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def display_weather(self, city: str):
        data = fetch_weather(city, self.api_key)
        if data:
            print_weather(data)
        else:
            print("Could not fetch weather data. Please check the city name or API key.")