import requests

def get_next_launch():
    url = "https://api.spacexdata.com/v4/launches/next"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch SpaceX data.")

    data = response.json()

    launch_name = data.get("name", "Unknown")
    launch_time = data.get("date_utc", "Unknown")
    launchpad_id = data.get("launchpad", "")

    pad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    pad_response = requests.get(pad_url)
    pad_data = pad_response.json()

    location = {
        "name": pad_data.get("name", "Unknown Site"),
        "latitude": pad_data.get("latitude", 0.0),
        "longitude": pad_data.get("longitude", 0.0)
    }

    return {
        "launch_name": launch_name,
        "launch_time": launch_time,
        "location": location
    }