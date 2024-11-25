from app.main.configuration import cfg
from app.extensions.log import log
from time import sleep
from app.extensions.mqtt import pub

class SensorPi:
    def __init__(self, beds, scd30):
        self.climateZoneID = cfg["climateZoneID"]
        self.mqttTopic = f"SYS/climateZone{self.climateZoneID}"
        
        self.beds = beds
        self.scd30 = scd30
        # this is a list of Bed objects and the SCD30 sensor object!
        
        log(f'sensorPi{self.climateZoneID}', True, 'app', 'setup', 'Successfully created the SensorPi app!')
        self.main()
        # start the app loop
    
    def main(self):
        ticksSinceLastSend = 0
        running = True
        
        while running:
            for bed in self.beds:
                # for every bed
                bed.tick()
                # take a reading
                if ticksSinceLastSend % 3 == 0:
                    bed.send(f"{self.mqttTopic}/bed{bed.bedNumber}")
                    pub.publish(f"{self.mqttTopic}/SCD30", self.scd30.takeReading())
                    
                else:
                    ticksSinceLastSend += 1  

            sleep(cfg["tickFrequency"])
            # wait until the next tick in required
            
    