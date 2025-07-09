# Weather Dashboard CLI

A simple command-line weather dashboard using the OpenWeatherMap API.

## Usage

1. **Get an API key** from [OpenWeatherMap](https://openweathermap.org/api).
2. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the dashboard:**
   ```
   python main.py "London,UK" --apikey YOUR_API_KEY
   ```

## Files

- `main.py`: Entry point
- `cli/`: CLI logic
- `dashboard/`: Dashboard logic
- `api/`: Weather API handler
- `utils/`: Output formatting

---

**You can extend this code to support more features, more APIs, or a web/GUI interface.**