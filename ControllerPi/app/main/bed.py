from app.extensions.log import log
from app.extensions.mqtt import sub
from app.main.configuration import cfg
from json import dump

class Bed:
    def __init__(self, wateringMethod, wateringSolenoid, climateZoneNumber, bedNumber, MQTTtopic):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.wateringMethod = wateringMethod
        # wateringMethod is the way the app determines when the watering solenoid should open.
        self.wateringSolenoid = wateringSolenoid
        # this is more hardware side of things.
        self.ticksSinceLastWatering = 0
        self.bedTemperature = None
        # runtime variables!
        self.czno = climateZoneNumber
        self.no = bedNumber
        self.MQTTtopic = MQTTtopic
                
        sub.subscribe(self.MQTTtopic, self.onSensorUpdate)
        
    def onSensorUpdate(self, data):
        data = dump(data)
        self.wateringMethod.soilMoistureSensorPercent = data["soilMoistureReading"]
        self.bedTemperature = data["temperatureReading"]

    def tick(self):
        if self.wateringMethod.tick():
            # if the wateringMethod belives we should water the plant, do!
            self.wateringSolenoid.open(seconds=cfg['tickFrequency'])
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids ', arg=f'climateZone:{self.czno}@bed{self.no}')
        else:
            self.ticksSinceLastWatering += 1
            # this variable is used by the timer 
