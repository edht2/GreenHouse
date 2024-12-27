from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from ControllerPi.app.greenhouse import GreenHouse
from ControllerPi.app.state.state import GREENHOUSE

app = GreenHouse(GREENHOUSE)
# create the GreenHouse object!!!