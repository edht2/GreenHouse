from app.config.config import state
from app.bed import Bed
from json import load

class ClimateZone:
    def __init__(self, climate_zone_number):
        self.climate_zone_number = climate_zone_number
        self.beds = [Bed(self.climate_zone_number, bed["bedNumber"]) for bed in state[self.climate_zone_number-1]["Beds"]]
        
    def update(self):
        for bed in self.beds:
            bed.update()
            # do an update!!
        
        state = load(open("app/config/state.json"))["climateZones"]
        
        """ Add climatezone temperature, humidity and co2 regulation here!! """