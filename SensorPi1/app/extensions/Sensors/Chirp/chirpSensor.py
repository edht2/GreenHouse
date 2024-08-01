from app.extensions.Sensors.Chirp.chirpFirmware import Chirp
import time
import os

# Initialize the sensor.
class ChirpSensor:
    def __init__(self, addr, no, min, max):
        self.no = no
        self.chirp = Chirp(bus=1, address=addr, min_moist=min, max_moist=max)
    
    def takeReading(self):
        self.sensor.trigger()
        return self.sensor.moist, self.sensor.temp