class Weather:
    def __init__(self, temp:float=0.0, precip:float=0.0, wind_sp:float=0.0) -> None:
        # a basic structure for weather
        self.temp = temp
        self.precip = precip
        self.wind_sp = wind_sp
        
    def __str__(self) -> str:
        # returns a string format of weather
        return f"temp: {self.temp}°C | precip: {self.precip}mm | wind_sp: {self.wind_sp}km/h"