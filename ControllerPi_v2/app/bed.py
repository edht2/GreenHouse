from app.config.config import state
from app.mqtt.mqtt import sub
from json import load

class Bed:
    def __init__(self, climate_zone_number, bed_number):
        
        # *** Important Indexes ***
        self.bed_number = bed_number
        self.climate_zone_number = climate_zone_number
        # *************************
        
        # **** Sensor Readings ****
        self.soil_moisture_percent = None
        self.bed_temperature = None
        # *************************

        sub().subscribe(f"{state[self.climate_zone_number-1]['climateZoneMQTTtopic']}/{state[climate_zone_number-1]['Beds'][bed_number-1]['MQTTtopic']}", self.on_sensor_update)
        # subscribe to the sensor data stream!

    def on_sensor_update(self, bed_data):

        bed_data = eval(bed_data)
        # turn the string dictionary into a python dict object

        self.soil_moisture_percent = bed_data["soil_moisture_reading"]
        self.bed_temperature = bed_data["temperature_reading"]
        # update the sensor readings
        
        print(f"Bed{self.bed_number} | soil_moisture: {self.soil_moisture_percent} bed_temp: {self.bed_temperature} status: {bed_data['status']}")


    def update(self):
        state = load(open("app/config/state.json"))["climateZones"]
        pass