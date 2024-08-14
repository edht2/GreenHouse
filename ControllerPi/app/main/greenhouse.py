from app.extensions.log import log
from app.extensions.mqtt import pub, sub
from app.main.configuration import cfg
from time import sleep

class GreenHouse:
    def __init__(self, gh):
        self.mqttBrokerAddr = cfg["mqttBrokerAddr"]
        self.tickFrequency = cfg["tickFrequency"]
        self.greenhouse = gh
        self.main()

    # this works asyncronously to the rest of the programme
    def main(self):
        while True:
            for climateZone in self.greenhouse["climateZones"]:
                climateZone.tick()
            sleep(self.tickFrequency())
