from colorama import Style, Fore, Back
from app.main.configuration import cfg
print(f"{Back.GREEN}{Fore.WHITE}Initiating SensorPi{cfg["climateZone"]}...{Style.RESET_ALL}")

from SensorPi1.app.main.sensorPi import SensorPi
from app.extensions.mqtt import sub, pub
from app.state import instantiateSensorPi
from app.main.configuration import cfg
from json import load

def onConfigResponce(data:str):
    # Awesome! We have our config now we can set up the SensorPi!
    SensorPi(instantiateSensorPi(load(data)))
    
sub.subscribe('SYS/setup', onConfigResponce)
pub.publish('SYS/setupRequest', f"climateZone : {cfg["climateZone"]}")


