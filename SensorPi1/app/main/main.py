from app.main.sensors import get_sensor_o_json
from app.main.conf import configure
from app.extensions.log import log
from app.extensions.utils import utils
from app.main.mqtt import MQTT
from time import sleep

class Main:
    def __init__(self, mqttBrokerAddr, climateZone, sendFrequency):
        self.mqttBrokerAddr = mqttBrokerAddr
        self.climateZone = climateZone
        self.sendFrequency = sendFrequency
        configure(mqttBrokerAddr, climateZone, sendFrequency)
        # update the config file
        log(f'sensorpi{climateZone}', True, 'app', 'setup', 'Successfully created the SensorPi app!')
        self.main()
        # start the app loop
    
    @utils.fire_and_forget
    # run the main loop seperatly to the rest of the programme 
    def main(self):
        while True:
            data = get_sensor_o_json()
            MQTT.send_sensor_data(data)
            sleep(self.sendFrequency)
            # wait until the next send in required
            
    