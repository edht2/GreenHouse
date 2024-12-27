""" This creates a listener waiting for a config from the controller pi then sends another message requesting this config. """

from colorama import Style, Fore, Back
from app.config import climate_zone_name
from app.main import sensorPi
from app.tools.state import instantiate_sensorpi

print(f"{Back.GREEN}{Fore.WHITE}Initiating {climate_zone_name}...{Style.RESET_ALL}")

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

beds, scd30 = instantiate_sensorpi(bed_dict)
# get the arguements for the sensor pi (beds and scd30)

sensorPi(beds=beds, scd30=scd30)
# instantiate the sensor pi