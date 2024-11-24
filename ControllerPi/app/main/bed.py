from app.extensions.log import log
from app.extensions.mqtt import sub
from app.main.configuration import cfg
from json import loads

class Bed:
    def __init__(self, wateringSolenoid, climateZoneNumber, bedNumber, MQTTtopic, soilMoisturePercentageRange):
        """ A bed comprises of a watering solenoid and a soil moisture sensor. """
        self.wateringSolenoid = wateringSolenoid
        
        # this is more hardware side of things.
        self.ticksSinceLastWatering = 0
        self.wateringTicks = 0
        
        # sensor readings
        self.bedTemperature = None
        self.soilMoistureSensorPercent = None
        
        # soil moisture percentage range this will be like 20% to 60% saturation
        # really there probibally is no need for gardeners to ever have to 
        self.soilMoisturePercentageRange = soilMoisturePercentageRange
        
        # runtime variables!
        self.czno = climateZoneNumber
        self.no = bedNumber
        self.MQTTtopic = MQTTtopic
                
        sub.subscribe(self.MQTTtopic, self.onSensorUpdate)
        
    def onSensorUpdate(self, data): # When we recive a bed package, we need to update the values 
        data = loads(data)
        # when the sensor pi sends a packet update the values accoringly
        self.soilMoistureSensorPercent = data["soilMoistureReading"]
        self.bedTemperature = data["temperatureReading"]

    def shouldWater(self): # determite if we should water! 
        if self.soilMoistureSensorPercent < self.soilMoisturePercentageRange[0]:
            # if the bed's soil-moisture saturation is below desired levels ↓
            print(f"Bed{self.no} is too dry: opening watering solenoid")
            return True
        
        if self.wateringSolenoid.state == 1:
            # so if the watering solenoid is open: keep watering until the 'soilMoistureSensorPercent' reaches the second value of 'soilMoisturePercentageRange' 
            return None
        
        if self.soilMoistureSensorPercent > self.soilMoisturePercentageRange[1]:
            # bed has been sufficiently watered: disable watering solenoid
            print(f"Bed{self.no}: Bed has been sufficiently watered: closing watering solenoid")
            return False

    def tick(self):
        sw = self.shouldWater()
        if sw:
            # OK, 'shouldWater()' says to water the bed
            self.wateringSolenoid.open(seconds=cfg['tickFrequency'])
            self.ticksSinceLastWatering = 0
            return log('ControllerPi', None, 'bed', 'wateringsolenoid', 'Opened the watering solenoids ', arg=f'climateZone:{self.czno}@bed{self.no}')
        
        elif sw == None:
            self.wateringTicks += 1
            # this variable can be used by the timer when that is implemented
            
        else:
            self.ticksSinceLastWatering += 1
            # again used by the timer