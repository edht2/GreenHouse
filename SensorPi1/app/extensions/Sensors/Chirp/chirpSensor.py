from app.extensions.Sensors.Chirp.chirpFirmware import Chirp
import time
import os

# Initialize the sensor.
class ChirpSensor:
    def __init__(self, address, no, min_moist, max_moist):
        self.no = no
        self.chirp = Chirp(bus=1, address=address, min_moist=min_moist, max_moist=max_moist)
    
    def takeReading(self):
        self.chirp.trigger()
        round_to = 5
        return round_to * round(self.chirp.moist_percent / round_to), self.chirp.temp