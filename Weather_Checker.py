import requests
from datetime import datetime

BASE_URL = "https://wttr.in"
search_history = []  # To store searched cities

WEATHER_EMOJIS = {
    "sunny": "☀️",
    "clear": "🌕",
    "cloudy": "☁️",
    "overcast": "☁️",
    "partly cloudy": "⛅",
    "rain": "🌧️",
    "thunder": "🌩️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌁"
}

def get_weather_emoji(description):
    desc = description.lower()
    for key in WEATHER_EMOJIS:
        if key in desc:
            return WEATHER_EMOJIS[key]
    return "🌈"  # Default icon

def fetch_weather_json(city: str):
    try:
        url = f"{BASE_URL}/{city}?format=j1"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print("❌ Network/API error:", e)
        return None

def show_current_weather(city: str):
    data = fetch_weather_json(city)
    if not data:
        return
    current = data["current_condition"][0]
    temp_c   = current["temp_C"]
    feels_c  = current["FeelsLikeC"]
    desc     = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind_kph = current["windspeedKmph"]
    emoji = get_weather_emoji(desc)

    print(f"\n{emoji}  Current weather in {city.title()}:")
    print(f"• {desc}")
    print(f"• Temperature : {temp_c} °C  (feels like {feels_c} °C)")
    print(f"• Humidity    : {humidity}%")
    print(f"• Wind speed  : {wind_kph} km/h")
    search_history.append(city.title())

def show_forecast(city: str):
    data = fetch_weather_json(city)
    if not data:
        return
    print(f"\n📅  3-Day Forecast for {city.title()}:")
    for day in data["weather"][:3]:
        date_str = day["date"]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        max_c = day["maxtempC"]
        min_c = day["mintempC"]
        desc  = day["hourly"][4]["weatherDesc"][0]["value"]
        emoji = get_weather_emoji(desc)
        print(f"{date_obj:%a %d %b}: {emoji} {desc:20} {min_c}–{max_c} °C")
    search_history.append(city.title())

def show_history():
    if not search_history:
        print("\n🕒 No search history yet.")
    else:
        print("\n📚 Previously searched cities:")
        for i, city in enumerate(search_history[-10:], 1):
            print(f"{i}. {city}")

def list_example_cities():
    print("\n🏙  Example city names: London | New York | Delhi | Tokyo | Sydney")

def main():
    print("=== 🌐 Real-Time Weather Checker ===")

    while True:
        print("\n📋 Menu")
        print("1. Current weather (single or multiple cities)")
        print("2. 3-Day forecast (single or multiple cities)")
        print("3. Show example cities")
        print("4. View search history")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            cities = input("Enter city/cities (comma-separated): ").split(',')
            for city in cities:
                show_current_weather(city.strip())
        elif choice == '2':
            cities = input("Enter city/cities (comma-separated): ").split(',')
            for city in cities:
                show_forecast(city.strip())
        elif choice == '3':
            list_example_cities()
        elif choice == '4':
            show_history()
        elif choice == '5':
            print("👋 Goodbye! Stay prepared for the weather.")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
