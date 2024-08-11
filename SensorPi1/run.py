from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating app...{Style.RESET_ALL}")

from app.main.main import climateZone
from app.extensions.mqtt import sub, pub
from app.state import instantiateSensorPi
from json import load

def onConfigResponce(data:str):
    # a json string will be sent
    app = climateZone(instantiateSensorPi(load(data)))

sub.subscribe('SYS/setup', onConfigResponce)
pub.publish('SYS/setupRequest', "requesting config!")


