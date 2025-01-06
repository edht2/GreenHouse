""" A class containing the whole greenhouse """
from app.config.config import state, update_frequency, device_name
from app.climate_zone import ClimateZone
from app.tools.log import log
from time import sleep
from json import load

class GreenHouse:
    def __init__(self):
        self.climate_zones = [ClimateZone(climate_zone["climateZoneNumber"]) for climate_zone in state]
        # create the climate zone object
        
        log(device_name, True, "app_setup", "conformation", "App has been successfuly setup")
        
        self.start_app_loop()
        
    def update(self):
        for climate_zone in self.climate_zones:
            climate_zone.update()
            # look at the sensor values, what is going on? fix it.
            
    def start_app_loop(self):
        
        while True:
            self.update()
            # trigger an update
            sleep(update_frequency)