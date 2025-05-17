Weather Checker (Console-Based)

A simple and user-friendly console-based weather application built in Python. It fetches real-time weather information and 3-day forecasts using the wttr.in API. 
Designed for users who want quick weather updates without opening a browser or app.

✨ Features

    🌤 Check current weather by city name

    📅 Get a 3-day forecast with temperature and descriptions

    😊 Emoji-based weather icons for easy visualization

    🏙 Supports multiple city inputs (e.g. Delhi, Mumbai, Tokyo)

    📜 Keeps a simple search history within the session

    ❌ Graceful handling of API or internet errors

    ✅ Clean and easy-to-use menu system
    
🧰 Tech Stack

    🐍 Python 3.x

    🌐 wttr.in (free weather API)

    📦 requests (HTTP client for API calls)

Follow the simple menu-driven interface:

    Current weather

    3-Day forecast

    Show example cities

    View search history

    Exit
    
📝 Sample Entry Flow

    Select: Current weather

    Enter: Delhi, Mumbai

    Output:
        🌤  Current weather in Delhi:
        • Clear
        • Temperature : 30 °C (feels like 32 °C)
        • Humidity    : 38%
        • Wind speed  : 12 km/h

        🌧️  Current weather in Mumbai:
        • Light rain
        • Temperature : 28 °C (feels like 30 °C)
        • Humidity    : 82%
        • Wind speed  : 18 km/h
        
📈 Future Improvements

     Add voice input using speech_recognition 🎙️
     
     GUI version using Tkinter 🖥️
     
     Save weather logs to a file 📝
     
     Add colored output (with colorama) 🌈

