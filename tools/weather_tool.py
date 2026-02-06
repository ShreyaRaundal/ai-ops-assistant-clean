import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_weather(city: str) -> dict:
    """
    Fetch current weather for a given city using OpenWeather API.
    """

    api_key = os.getenv("WEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Handle API error safely
    if response.status_code != 200:
        return {
            "error": f"Could not fetch weather for {city}"
        }

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
