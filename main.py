from spacex_agent import get_next_launch
from weather_agent import get_weather_forecast
from summary_agent import analyze_launch_conditions

def run_pipeline():
    print("\n🚀 Starting Multi-Agent AI System...\n")

    print("🛰 Fetching next SpaceX launch info...")
    launch_info = get_next_launch()
    print(f"  ➤ Launch Name : {launch_info['launch_name']}")
    print(f"  ➤ Launch Time : {launch_info['launch_time']}")
    print(f"  ➤ Launch Site : {launch_info['location']['name']}\n")

    print("🌦 Fetching weather forecast at launch site...")
    lat = launch_info['location']['latitude']
    lon = launch_info['location']['longitude']
    launch_time = launch_info['launch_time']

    weather = get_weather_forecast(lat, lon, launch_time)
    print(f"  ➤ Temperature     : {weather['temperature_c']}°C")
    print(f"  ➤ Precipitation   : {weather['precipitation_mm']} mm")
    print(f"  ➤ Wind Speed      : {weather['wind_speed_kmh']} km/h\n")

    print("🔍 Analyzing conditions for potential delay...")
    summary = analyze_launch_conditions(weather)

    print(f"\n📋 Final Status     : {summary['status']}")
    for reason in summary['reasons']:
        print(f"  - {reason}")
    print(f"💡 Advice           : {summary['advice']}")
    print("\n✅ Pipeline Complete.\n")

if __name__ == "__main__":
    run_pipeline()