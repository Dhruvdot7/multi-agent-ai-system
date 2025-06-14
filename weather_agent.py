import requests
from datetime import datetime

def get_weather_forecast(lat, lon, launch_time_utc):
    base_url = "https://api.open-meteo.com/v1/forecast"

    # Convert launch time to datetime
    launch_dt = datetime.fromisoformat(launch_time_utc.replace("Z", "+00:00"))
    launch_date = launch_dt.date().isoformat()
    launch_hour = launch_dt.hour
    hour_string = f"{launch_date}T{launch_hour:02d}:00"

    # Prepare API request
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "start_date": launch_date,
        "end_date": launch_date,
        "timezone": "UTC"
    }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch weather data.")

    data = response.json()

    # Debug print: Check available times
    print(">> Hourly times from API:", data["hourly"]["time"])
    print(">> Looking for hour:", hour_string)

    hourly_time = data["hourly"]["time"]
    temp = data["hourly"].get("temperature_2m", [])
    rain = data["hourly"].get("precipitation", [])
    wind = data["hourly"].get("wind_speed_10m", [])

    # Debug: log weather arrays
    print(">> Temp values:", temp)
    print(">> Rain values:", rain)
    print(">> Wind values:", wind)

    # Find the index for the launch hour
    index = next((i for i, t in enumerate(hourly_time) if t == hour_string), None)
    if index is None:
        raise Exception("No weather data found for launch time.")

    # Extract weather info safely with defaults
    weather_at_launch = {
        "temperature_c": temp[index] if index < len(temp) and temp[index] is not None else 0.0,
        "precipitation_mm": rain[index] if index < len(rain) and rain[index] is not None else 0.0,
        "wind_speed_kmh": wind[index] if index < len(wind) and wind[index] is not None else 0.0
    }

    print(">> Weather at launch hour:", weather_at_launch)

    return weather_at_launch
