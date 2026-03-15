def get_weather(city):

    fake_weather = {
        "Los Angeles": "22°C Sunny",
        "New York": "15°C Cloudy"
    }

    return fake_weather.get(city, "Weather unknown")