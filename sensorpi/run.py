""" This creates a listener waiting for a config from the controller pi then sends another message requesting this config. """

from colorama import Style, Fore, Back
from app.config import climate_zone_name, chirpsensor_i2c_address, chirp_sensor_cal, bed_num
from app.main import sensorPi
from app.tools.state import instantiate_sensorpi

print(f"{Back.GREEN}{Fore.WHITE}Initiating {climate_zone_name}...{Style.RESET_ALL}")


""" create a dictionary for the climate zone which includes the bed id number, the i2c addresses for each of the 
    soil moisture sensors and the calibration data for them. """

bed_dictionary = {"beds" : []}
# create a dictionary with one item called beds which is an empty list

for x in range(len(bed_num)): 
# loop x times to reflect the number of beds in each climate zone. 
    
    bed = dict(chirp_sensor_i2c_address = chirpsensor_i2c_address[x], 
               chirp_sensor_calibration = chirp_sensor_cal[x], 
               bed_number = bed_num[x], 
               mqtt_topic = f"bed{bed_num[x]}")
    # create a 'bed' dictionary with attributes from config.py 
    
    bed_dictionary["beds"].append(bed)
    # append each 'bed' dictionary to the 'beds' dictionary list


beds, scd30 = instantiate_sensorpi(bed_dictionary)
# get the arguments for the sensor pi (beds and scd30)

sensorPi(beds=beds, scd30=scd30)
# instantiate the sensor pi
