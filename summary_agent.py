def analyze_launch_conditions(weather):
    temperature = weather.get("temperature_c") or 0
    precipitation = weather.get("precipitation_mm") or 0
    wind_speed = weather.get("wind_speed_kmh") or 0

    reasons = []

    if precipitation is not None and precipitation > 1.0:
        reasons.append("High chance of rain")
    if wind_speed > 30:
        reasons.append("Strong winds may affect the launch")

    if reasons:
        summary = {
            "status": "Possibly delayed",
            "reasons": reasons,
            "advice": "Monitor weather updates near launch time."
        }
    else:
        summary = {
            "status": "Launch likely on time",
            "reasons": ["Weather conditions are within safe limits"],
            "advice": "No severe weather detected at launch site."
        }

    return summary