from app.config.config import state
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
        
        log('OK', 'climatezone', 'init', 'Beds initialised for climate-zone', arg=self.climate_zone_number)
        # log progess
        
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
        
        log('OK', 'climatezone', 'init', 'Window acctuators initialised for climate-zone', arg=self.climate_zone_number)
        
        # +++++++
        # WATERING SOLENOIDS
        # +++++++
        
        log('OK', "climatezone", "init", f"Successfuly initialised climate-zone", arg=self.climate_zone_number)
        # log the climate-zone has been created!
        
        
    def update(self) -> None:
        
        for bed in self.beds:
            
            bed.update()
            # do an update!!
        
        state = load(open("app/config/state.json"))["climateZones"]
        # reload state incase there were any changes to the ranges and tergets
        
        """ Add climatezone temperature, humidity and co2 regulation here!! """