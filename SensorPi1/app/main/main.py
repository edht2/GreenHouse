from app.main.sensors import get_sensor_o_dict
from app.main.configuration import cfg
from app.extensions.log import log
from app.main.mqtt import MQTT
from time import sleep

class climateZone:
    def __init__(self, beds, scd30):
        self.mqttBrokerAddr = cfg["mqttBrokerAddr"]
        self.climateZone    = cfg["climateZone"]
        self.sendFrequency  = cfg["sendFrequency"]
        self.readFrequency  = cfg["readFrequency"]
        self.mqttTopic = f"SYS/climateZone{self.climateZone}"
        
        self.beds = beds
        self.scd30 = scd30
        
        # update the config file
        log(f'sensorPi{self.climateZone}', True, 'app', 'setup', 'Successfully created the SensorPi app!')
        self.main()
        # start the app loop
    
    # run the main loop seperatly to the rest of the programme 
    def main(self):
        while True:
            counter = 0
            for bed in self.beds:
                bed.tick()
                if counter % 3:
                    bed.send(f"{self.mqttTopic}/bed{bed.bedNumber}")
                else:
                    counter += 1
            
            data = get_sensor_o_dict()
            MQTT.send_sensor_data(data)
            log(f'sensorPi{self.climateZone}', True, 'app', 'mqtt', 'Sent new sensor data packet')
            sleep(self.sendFrequency)
            
            # wait until the next send in required
            
    