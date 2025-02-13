import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = b"gsddfshdlviuiHJHJHHduyfyify847f7wchri8oJMOMU&rd8FD8wper8fuwp9f8eurgjsdlvud8gusdfigudsfh8g79p8h8rtugjfijdjb"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'var/test/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


send_frequency = 30 
# how often data is sent to the controller pi

mqtt_broker_address ="mqtt.eclipseprojects.io"
# the mqtt broker address to which we publish the environment limits
# the controller pi will be able to see the latest environment limits which is updated on start up of flask 
# and on submitting of the environment limits (Green House) page

mqtt_topic = "env_limits"
# where all of the data exported is directed through
    
