from app.extensions.log import log
from app.wateringMethods.soilmoisture import SM
from app.extensions.utils import utils

class Bed:
    def __init__(self, wateringSolendoid, no, cliZone):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.wateringMethod = SM()
        #ranges
        self.moistureRange = [30, 45]
        # hardware
        self.ws = wateringSolendoid
        # runtime
        self.ticksSinceLastWatering = 0
        self.smsf = 20
        # default value
        self.smsHistory = utils.meanSensorData([], self.smsf)
        self.no = no
        self.czno = cliZone

    def tick(self):
        if self.wateringMethod.tick(self.ws, self.moistureRange, self.smsf):
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids ', arg=f'climateZone:{self.czno}@bed{self.no}')
    
