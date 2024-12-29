from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from app.greenhouse import GreenHouse
from app.state.state import GREEN_HOUSE

app = GreenHouse(GREEN_HOUSE)
# create the GreenHouse object!!!
