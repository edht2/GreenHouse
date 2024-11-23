from app.main.configuration import cfg
from app.extensions.log import log
from time import sleep
from app.extensions.mqtt import pub

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
    
    def main(self):
        ticksSinceLastSend = 0
        
        while True:
            # just forever
            for bed in self.beds:
                # for every bed
                bed.tick()
                # take a reading
                if ticksSinceLastSend % 3:
                    bed.send(f"{self.mqttTopic}/bed{bed.bedNumber}")
                else:
                    ticksSinceLastSend += 1
            
            pub.publish(f"{self.mqttTopic}/SCD30", self.scd30.takeReading())

            sleep(self.sendFrequency)
            # wait until the next send in required
            
    