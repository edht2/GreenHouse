from app.sensors.Chirp.chirp_firmware import Chirp

class ChirpSensor:
    def __init__(self, I2C_address, number, min_moist, max_moist):
        self.number = number
        # the number assigned to the sensor
        
        self.chirp = Chirp(bus=1, address=I2C_address, min_moist=min_moist, max_moist=max_moist)
        # create the chirp interface
    
    def read(self):
        self.chirp.trigger()
        # call the sensor to take a reading
        
        return self.chirp.moist_percent, self.chirp.temp
