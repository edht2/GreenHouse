from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from app.mqtt.mqtt import sub

def sd(msg):
    print("msg", msg)
sub.subscribe("climate_zone_1", sd)

from app.greenhouse import GreenHouse
from app.state.state import GREEN_HOUSE

app = GreenHouse(GREEN_HOUSE)
# create the GreenHouse object!!!
