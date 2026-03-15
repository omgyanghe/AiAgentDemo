def get_weather(city):
    """
    获取城市天气

    :param city: 城市名称
    :return: 城市天气信息
    """

    fake_weather = {
        "Los Angeles": "22°C Sunny",
        "New York": "15°C Cloudy"
    }

    return fake_weather.get(city, "Weather unknown")