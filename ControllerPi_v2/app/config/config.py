from json import load

state = load(open("app/config/state.json"))
# state contains all of the target / hardware information to run the greenhouse

mqtt_broker_address = "mqtt.eclipseprojects.io"