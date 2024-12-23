climate_zone_number = 1
# the number assigned to the c.z.

climate_zone_name = f"sensorPi {climate_zone_number}"
# the name of the climate zone

read_frequency = 10
# how often the sensors are triggered

send_frequency = 30 
# how often data is sent to the controller pi

mqtt_broker_address ="mqtt.eclipseprojects.io"
# the mqtt broker address is a cruicial part of the system allowing the sensor pi
# to communicate with the controller pi
mqtt_topic = f"climate_zone_{climate_zone_number}"
# where all of the data exported is directed through