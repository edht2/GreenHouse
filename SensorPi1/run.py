""" This creates a listener waiting for a config from the controller pi then sends another message requesting this config. """

from colorama import Style, Fore, Back
from app.config import climate_zone_number, climate_zone_name
from app.main import sensorPi
from app.mqtt.mqtt import sub, pub
from app.tools.state import instantiate_sensorpi
from json import loads, dumps

"""
def on_config_response(data):
    # Awesome! We have our config now we can set up the SensorPi!
    
    print(f"{Back.GREEN}{Fore.WHITE}Initiating {climate_zone_name}...{Style.RESET_ALL}")
    # print a cool looking message confirming it is working
    
    sensorPi(instantiate_sensorpi(loads(data)))
    
sub.subscribe(f'setup_climate_zone_{climate_zone_number}', on_config_response)
pub.publish(f'setup_request_climate_zone_{climate_zone_number}', f"climate_zone : {climate_zone_number}")
"""

# ** test script remove in live env **
bed_dict = {
    "beds" : [
        {
            "chirpSensorI2CAddress" : 0x10,
            "chirpSensorCalibration" : [200, 530],
            "bedNumber" : 1,
            "MQTTtopic" : "bed1"
        },
        {
            "chirpSensorI2CAddress" : 0x11,
            "chirpSensorCalibration" : [200, 530],
            "bedNumber" : 2,
            "MQTTtopic" : "bed2"
        }
    ]
}



data = bed_dict

a = instantiate_sensorpi(data)

sensorPi(beds=a[0], scd30=a[1])
