from app.extensions.utils import utils
from app.main.conf import sensorSendFrequency
from time import sleep
from app.main.conf import tickFrequency
from app.extensions.log import log

class SM:
    def __init__(self, targetMoistureRange, chirpSensorI2CAddress):
        """ SM class is a watering method - the default one (also the best).
        This reads the soil's moisture content and waters it accoringly, very simple! """
        self.watering = True
        # watering:bool will determine if it should water until the soil moisture is at the top of the range
        self.targetMoistureRange = targetMoistureRange
        self.chirpSensorI2CAddress = chirpSensorI2CAddress
        # we will not need the chirp sensor I2C address for tick, but more as just storing the value
    
    def tick(self, soilMoistureSensorPercent):
        if self.watering:
            # if we are topping up the bed
            if soilMoistureSensorPercent > self.targetMoistureRange[1]:
                self.watering = False
                return False
            return True

        elif soilMoistureSensorPercent < self.targetMoistureRange[0]:
		    # too dry and not being watered
            self.watering = True
            return True
            
        
            
