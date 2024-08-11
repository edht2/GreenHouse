from app.extensions.Sensors.Chirp.chirpSensor import ChirpSensor
from app.extensions.mqtt import pub
from app.extensions.utils import utils
from app.extensions.log import log
from app.main.configuration import cfg
from json import dump

class Bed:
    def __init__(self, chirpSensorI2CAddress, chirpSensorCalibration, bedNumber):        
        self.chirpSensorI2CAddress = chirpSensorI2CAddress
        self.chirpSensorCalibration = chirpSensorCalibration
        self.bedNumber = bedNumber
        
        self.chirpSensor = ChirpSensor(self.chirpSensorI2CAddress, self.bedNumber, self.chirpSensorCalibration[0], self.chirpSensorCalibration[1])
        
        self.soilMoistureReadings = []
        self.temperatureReadings = []
        self.status = "OK"
    
    @utils.fire_and_forget
    def tick(self):
        try:
            reading = self.chirpSensor.takeReading()
            self.soilMoistureReadings.append(reading[0])
            self.temperatureReadings.appen(reading[1])
            # I add the read sensor values to a list to later be turned into mean average of the list.
            # I do this to reduce chance of a faulty reading messing everything up!
        except Exception as e:
            log(f"SensorPi{cfg["climateZone"]}", False, "bed", "chirpsensorreading",  "Error while trying to read sensor data, entering safe mode...", error=e)
            self.status = "ER"
            # by setting the status to 'ER', the controller pi now knows to stop using this soil moisture sensor, and instead uses the clock.
        
        
    def send(self, mqttTopic):
        message = dump({
            "soilMoistureReading" : utils.mean(self.soilMoistureReadings),
            "temperatureReading" : utils.mean(self.temperatureReadings),
            "status" : self.status
        })
        self.soilMoistureReadings = []
        self.temperatureReadings = []
        
        pub.publish(mqttTopic, message)