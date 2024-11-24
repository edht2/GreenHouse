from app.extensions.log import log
from app.extensions.mqtt import pub, sub
from app.main.configuration import cfg
from time import sleep

class GreenHouse:
    def __init__(self, gh):
        self.greenHouseObjects = gh
        self.main()
        # start the greenhouse loop!

    def main(self):
        while True:
            for climateZone in self.greenHouseObjects:
                climateZone.tick()
            sleep(cfg["tickFrequency"])
