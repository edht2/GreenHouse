from app.extensions.log import log
from app.wateringMethods.soilmoisture import SM
from app.extensions.utils import utils

class Bed:
    def __init__(self, soilMoistureSensorFloat, wateringSolendoid):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.watering_method = SM()
        #ranges
        self.moistureRange = [30, 45]
        # hardware
        self.ws = wateringSolendoid
        # runtime
        self.ticksSinceLastWatering = 0
        self.sms = soilMoistureSensorFloat
        self.smsHistory = utils.meanSensorData([], soilMoistureSensorFloat)
    
    def tick(self):
        if SM.tick(self):
            self.ws.open(seconds=self.watering_method.time)
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids...')
    