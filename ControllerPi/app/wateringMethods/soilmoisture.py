from app.extensions.utils import utils
from app.extensions.log import log

class SM:
    def __init__(self, targetMoistureRange, chirpSensorI2CAddress, chirpSensorCalibration):
        """ SM class is a watering method - the default one (also the best).
        This reads the soil's moisture content and waters it accoringly, very simple! """
        self.watering = True
        # watering:bool will determine if it should water until the soil moisture is at the top of the range
        self.targetMoistureRange = targetMoistureRange
        self.chirpSensorI2CAddress = chirpSensorI2CAddress
        self.chirpSensorCalibration = chirpSensorCalibration
        # we will not need the chirp sensor I2C address for tick nor the calibnration, but more as just storing the value
        self.soilMoistureSensorPercent = None
    
    def tick(self):
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
            
        
            
