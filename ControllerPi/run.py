from colorama import Style, Fore, Back
print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")

from app.extensions.mqtt import pub, sub
from app.extensions.utils import utils
from app.main.greenhouse import GreenHouse
from app.state.greenhouse import onConfigRequest, GREENHOUSE


""" I think this is a bit hard to understand, so I will try here:
The Controler Pi is started before any of the sensor pis. When the controller pi has booted, An MQTT listener is created
sensing a message in the 'SYS/setupRequest' MQTT topic. A sensor pi (when turned on) will publish to this topic stating
its climateZoneNumber. The controller pi reads this and return another message with all of the information about that
sensor pi in question. It sends this in the MQTT topic 'SYS/setup< climateZoneNumber >' This returned string has lots
of information including sensor calibration and I²C addresses. """

@utils.fire_and_forget
def setupResponse(data):
    # This function is called when a sensor pi requests their configuation
    config, climateZoneNumber = onConfigRequest(data)
    # OnConfigRequest returns the sensor pi's config!
    pub.publish(f"SYS/setup{climateZoneNumber}", config)

sub.subscribe('SYS/setupReqest', setupResponse)
# Here we setup the lister the controller pi has ↑

""" Great! We have setup the listener. Now we can move on looking at the greenhouse! We create the greenhouse object
as easily as you would have guessed. It's one parameter is 'GREENHOUSE'. This pram. is crucial as it tells the
greenhouse what it is made of. The pram. is a list of the climate zone objects. """

app = GreenHouse(GREENHOUSE)
# create the GreenHouse object!!!

