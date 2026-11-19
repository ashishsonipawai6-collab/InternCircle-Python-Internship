
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            CURRENT_URL, params=params, timeout=10
        )
        response.raise_for_status()

        data = response.json()

        print("\n------ CURRENT WEATHER ------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("City not found!")
        elif response.status_code == 401:
            print("Invalid API key or key not activated!")
        else:
            print("Weather API error:", response.status_code)
        return

    except requests.exceptions.RequestException as error:
        print("Network error:", error)
        return

    # Fetch forecast
    try:
        forecast_params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        forecast_response = requests.get(
            FORECAST_URL,
            params=forecast_params,
            timeout=10
        )
        forecast_response.raise_for_status()

        forecast_data = forecast_response.json()

        print("\n------ UPCOMING FORECAST ------")

        for item in forecast_data["list"][:5]:
            date_time = item["dt_txt"]
            temperature = item["main"]["temp"]
            condition = item["weather"][0]["description"]

            print("\nDate & Time:", date_time)
            print("Temperature:", temperature, "°C")
            print("Condition:", condition)

    except requests.exceptions.RequestException as error:
        print("Forecast error:", error)


def main():
    if not API_KEY:
        print("API key missing! Check your .env file.")
        return

    print("===== WEATHER APP =====")

    while True:
        city = input("\nEnter city name (or exit): ").strip()

        if city.lower() == "exit":
            print("Thank you for using Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
