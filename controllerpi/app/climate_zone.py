from app.config.config import state, device_name
from app.tools.log import log
from app.control.actuator import Actuator
from app.bed import Bed
from json import load

class ClimateZone:
    def __init__(self, climate_zone_number: int) -> None:
        self.climate_zone_number = climate_zone_number
        
        self.beds = [
            Bed(self.climate_zone_number, bed["bedNumber"]) 
            for bed in state[self.climate_zone_number-1]["Beds"]]
        # gets all of the beds and creates a bed object for each one
        
        self.side_windows = [Actuator([
            actuator_sw["actuatorRelayIndexExtend"], 
            actuator_sw["actuatorRelayIndexRetract"]],
            extension_time=40
        ) for actuator_sw in state[self.climate_zone_number-1]["sideWindows"]]
        # creates all of the side_windows in the actuator class so you can type 'side_window[index].extend()'
        
        self.top_windows = [Actuator([
            actuator_tw["actuatorRelayIndexExtend"], 
            actuator_tw["actuatorRelayIndexRetract"]],
            extension_time=60
        ) for actuator_tw in state[self.climate_zone_number-1]["topWindows"]]
        # locate the addresses of the top and side windows then initialise them to the Actuator object
        
        log(device_name, True, "climatezone", "init", f"Climate-zone {self.climate_zone_number} has been created")
        # log the climate-zone has been created!
        
    def update(self) -> None:
        for bed in self.beds:
            bed.update()
            # do an update!!
        
        state = load(open("app/config/state.json"))["climateZones"]
        
        """ Add climatezone temperature, humidity and co2 regulation here!! """