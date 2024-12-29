from app.tools.log import log
from app.mqtt.mqtt import sub
from app.config import tick_frequency
from time import sleep

class GreenHouse:
    def __init__(self, gh):
        self.green_house = gh
        # A list of every climate zone which contain everything else, from beds to solenoids
        
        sub.subscribe("gerbil", self.sd)
        
        self.main()
        # start the greenhouse loop!

    def sd(self, data):
        print(data)

    def main(self):
        while True:
            for climate_zone in self.green_house:
                
                climate_zone.tick()
                # triggering a tick on a climate zone causes each bed to get watered ( if needed )
                
            sleep(tick_frequency)
            # wait until the next tick is needed
