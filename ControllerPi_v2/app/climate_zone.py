from app.config.config import state

class ClimateZone:
    def __init__(self, climate_zone_number):
        self.climate_zone_number = climate_zone_number
        
    def tick(self):
        print("tick at:", self.climate_zone_number)
    