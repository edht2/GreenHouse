from app.config import read_frequency, mqtt_topic, climate_zone_name, climate_zone_number
from app.tools.log import log
from time import sleep
from app.mqtt.mqtt import pub
from json import dumps

class sensorPi:
    def __init__(self, beds, scd30):
        self.beds = beds
        self.scd30_sensor = scd30
        # this is a list of Bed objects and the SCD30 sensor object!
        
        log(climate_zone_name, True, 'app', 'setup', 'Successfully created the sensorPi app!')
        # log the sensorpi is working
        
        self.main_loop()
        # start the app loop
    
    def main_loop(self):
        ticks_counter = 0
        running = True
        
        while running:
            for bed in self.beds: bed.sample_readings()
            self.scd30_sensor.read()
            # takes a readings

            if ticks_counter % 3 == 0:
                message = {
                    "climate_zone_number" : climate_zone_number,
                    "beds" : []     
                }
                # create a dictionary to store the message

                for bed in self.beds: message["beds"].append(bed.compile_data())               
                scd30_data = self.scd30_sensor.compile_data()
                # get the scd30 data
                
                message["CO2ppm"] = scd30_data["CO2ppm"]
                message["temperature"] = scd30_data["temperature"]
                message["RH%"] = scd30_data["RH%"]
                # add the scd30 sensor data to the message
                
                pub.publish(mqtt_topic, dumps(message))
                # send the new data to the controller pi
                
                print(dumps(message))
                
                log(climate_zone_name, True, "send_data", "conformation", "Successfuly sent new data packet")
                # log the success!
            
            ticks_counter += 1  

            sleep(read_frequency)
            # wait until the next tick in required
