from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from app.extensions.mqtt import pub, sub
from app.extensions.utils import utils
from app.main.greenhouse import GreenHouse
from app.state.greenhouse import onConfigRequest, GREENHOUSE

@utils.fire_and_forget
def setupResponse(data):
    print("GERBSISDADASD")
    config = onConfigRequest(data)
    pub.publish('SYS/setup', config)
    # the climate zone should change based on the current climatezones

sub.subscribe('SYS/setupReqest', setupResponse)
# this is the listener for a sensor pi to connect

app = GreenHouse(GREENHOUSE)
# create the GreenHouse object!!!
