from json import load

device_name = "controllerpi"
# the unique name assigned to the pi

mqtt_broker_address = "mqtt.eclipseprojects.io"
# the broker address used by the greenhouse

update_frequency = 30
# update every 30 seconds

max_ticks_without_data = 5
# after 5 consecutive ticks from a bed without data then go into safe mode

state = load(open("app/config/state.json"))["climateZones"]
# state contains all of the target / hardware information to run the greenhouse