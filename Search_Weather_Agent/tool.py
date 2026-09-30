

from langchain_nimble import NimbleSearchTool
from langchain.tools import tool
import os
import requests

search_tool = NimbleSearchTool(
    k = 5,
    deep_search = True,
    parsing_type = "markdown"
)



def google_search(query:str):
    """" 
    search anything on google for real time information.
    Args:
        query - user search query for google serach
    Return - result from google search
    """
    res = search_tool.invoke(query)
    return res


def weather_tool(city):
    """
        Get real time weather details like temperture, humidity and others.
        Args:
            city - city name for weather details]
        Return -> weather data from api response.
    """
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHR_API_KEY')}"
    res = requests.get(API_URL)
    if res.status_code == 200:
        return res.json()

    return "Unable to find details for this city"

ALL_TOOLS = [google_search, weather_tool]

