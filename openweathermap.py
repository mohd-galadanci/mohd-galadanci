import requests

def fetch_weather(city: str, api_key: str) -> dict | None:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"API error: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"Network error: {e}")
    return None