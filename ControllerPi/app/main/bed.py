from app.extensions.log import log
from app.extensions.utils import utils
from app.main.conf import cfg

class Bed:
    def __init__(self, wateringMethod, wateringSolendoid, climateZoneNumber, bedNumber):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.wateringMethod = wateringMethod
        self.wateringSolendoid = wateringSolendoid

        self.ticksSinceLastWatering = 0
        self.soilMoisturePercent = 20

        self.smsHistory = utils.meanSensorData([], self.smsf)
        self.czno = climateZoneNumber
        self.no = bedNumber

    def tick(self):
        if self.wateringMethod.tick(self.soilMoisturePercent):
            # if the wateringMethod belives we should water the plant, do!
            self.wateringSolendoid.open(seconds=cfg['tickFrequency'])
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids ', arg=f'climateZone:{self.czno}@bed{self.no}')
    
