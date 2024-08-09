from app.extensions.log import log
from app.extensions.mqtt import pub, sub
from app.extensions.utils import utils
from app.main.conf import mqttBrokerAddr, tickFrequency
from app.state.greenhouse import czs
from time import sleep

class Main:
    def __init__(self):
        self.mqttBrokerAddr = mqttBrokerAddr
        self.tickFrequency = tickFrequency
        self.climateZones = czs
        self.main()

    # this works asyncronously to the rest of the programme
    def main(self):
        while True:
            for climateZone in self.climateZones:
                climateZone.tick()
            sleep(self.tickFrequency())
