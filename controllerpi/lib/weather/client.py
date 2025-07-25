""" Using open-meteo weather api as it is accurate and free! This class is used
for obtaining weather data for the green-house in-order to releave rain and wind
damage and prepare for future storms etc. """

import requests
from lib.weather.weather import Weather
from app.config.config import latitude, longitude

class Client:
    
    def get_current() -> Weather:
        curr = requests.get(f"api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m,precipitation")
        # get json data, requests turns it into a python dictionary
        
        return Weather(temp=curr["temperature_2m"], precip=curr["precipitation"], wind_sp=curr["wind_speed_10m"])
        # return weather data