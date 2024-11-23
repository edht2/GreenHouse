from colorama import Style, Fore, Back
from app.main.configuration import cfg
print(f"{Back.GREEN}{Fore.WHITE}Initiating SensorPi{cfg["climateZone"]}...{Style.RESET_ALL}")

from SensorPi1.app.main.climatezone import climateZone
from app.extensions.mqtt import sub, pub
from app.state import instantiateSensorPi
from app.main.configuration import cfg
from json import load

def onConfigResponce(data:str):
    # a json string will be sent
    app = climateZone(instantiateSensorPi(load(data)))
    
sub.subscribe('SYS/setup', onConfigResponce)
pub.publish('SYS/setupRequest', f"climateZone : {cfg["climateZone"]}")


