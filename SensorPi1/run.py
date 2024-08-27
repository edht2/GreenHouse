from colorama import Style, Fore, Back
from app.main.configuration import cfg
print(f"{Back.GREEN}{Fore.WHITE}Initiating SensorPi{cfg["climateZone"]}...{Style.RESET_ALL}")

from app.main.main import climateZone
from app.extensions.mqtt import sub, pub
from app.state import instantiateSensorPi
from json import load

def onConfigResponce(data:str):
    print("GERBILS!")
    # a json string will be sent
    app = climateZone(instantiateSensorPi(load(data)))

sub.subscribe('SYS/setup', onConfigResponce)
pub.publish('SYS/setupRequest', "requesting config!")


