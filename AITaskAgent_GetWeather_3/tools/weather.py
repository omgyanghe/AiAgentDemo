# Debug 时，添加项目根目录到 Python 路径
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests
from tools.decorator import tool

# @tool
# def get_weather(city: str):
#     """
#     获取指定城市的天气信息
    
#     :param city: 城市名称
#     :return: 天气信息
#     """
#     fake_weather = {
#         "Los Angeles": "22°C Sunny",
#         "New York": "15°C Cloudy",
#         "Beijing": "25°C Sunny",
#         "Shanghai": "28°C Rainy",
#         "Tokyo": "20°C Cloudy",
#         "London": "12°C Rainy",
#         "Paris": "18°C Sunny"
#     }

#     return fake_weather.get(city, f"Weather for {city} unknown")

@tool
def get_weather(city: str):

    """Get current weather of a city"""

    url = f"https://wttr.in/{city}?format=3"

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    print(get_weather("beijing"))
