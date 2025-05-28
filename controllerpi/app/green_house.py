""" A class containing the whole greenhouse """
from app.config.config import state, update_frequency, device_name
from app.climate_zone import ClimateZone
from app.tools.log import log
from time import sleep

class GreenHouse:
    def __init__(self) -> None:
        self.climate_zones = [ClimateZone(climate_zone["climateZoneNumber"]) for climate_zone in state]
        # create the climate zone object
        
        log(device_name, True, "greenhouse", "init", "App has been successfuly setup")
        print("-" * 70)
        
        self.start_app_loop()
        
    def update(self) -> None:
        for climate_zone in self.climate_zones:
            climate_zone.update()
            # look at the sensor values, what is going on? fix it.
            
    def start_app_loop(self) -> None:
        while True:
            try:
                log(device_name, None, "greenhouse", "app_loop", "Triggering new update")
                self.update()
                # trigger an update
                log(device_name, True, "greenhouse", "app_loop", "Successfuly performed an update")
            except Exception as e:
                log(device_name, False, "greenhouse", "app_loop", "Failed to perform update", error=e)
                
            sleep(update_frequency)