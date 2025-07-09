import argparse
from dashboard.dashboard import WeatherDashboard

def main():
    parser = argparse.ArgumentParser(description="Weather Dashboard CLI")
    parser.add_argument("city", type=str, help="City name (e.g., London,UK or Paris,FR)")
    parser.add_argument("--apikey", type=str, required=True, help="OpenWeatherMap API Key")
    args = parser.parse_args()

    dashboard = WeatherDashboard(api_key=args.apikey)
    dashboard.display_weather(args.city)