import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = b"gsddfshdlviuiHJHJHHduyfyify847f7wchri8oJMOMU&rd8FD8wper8fuwp9f8eurgjsdlvud8gusdfigudsfh8g79p8h8rtugjfijdjb"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(BASEDIR, 'var/test/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MQTT_LIMIT_TOPIC = "env_limits"
    # where all of the data exported is directed through
    MQTT_SENSOR_TOPIC = ["climate_zone_1/#", "climate_zone_2/#"]
    MQTT_BROKER_ADDRESS ="mqtt.eclipseprojects.io"
    MQTT_PORT = 1883



SEND_FREQUENCY = 30 
# how often data is sent to the controller pi


MQTT_BROKER_ADDRESS ="mqtt.eclipseprojects.io"
# the mqtt broker address to which we publish the environment limits
# the controller pi will be able to see the latest environment limits which is updated on start up of flask 
# and on submitting of the environment limits (Green House) page


BED_NUM = 8
# no of soil moisture readers in the greenhouse (represented by beds)

NO_OF_BEDS_IN_CZ1 = 3
