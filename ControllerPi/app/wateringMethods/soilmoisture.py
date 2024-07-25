from app.extensions.utils import utils
from app.main.conf import sensorSendFrequency
from time import sleep
from app.main.conf import tickFrequency
from app.extensions.log import log

class SM:
    def __init__(self):
        """ SM class is a watering method - the default one (also the best).
        This reads the soil's moisture content and waters it accoringly, very simple! """
        self.watering = True
    
    def tick(self, wateringSolenoid, moistureRange, soilMoistureSensorFloat):
        if moistureRange[0] > soilMoistureSensorFloat:
            if wateringSolenoid.state == 0:
		# too dry and not being watered
                wateringSolenoid.open(tickFrequency())
                self.watering = True
                # enable watering for 30 seconds, or what ever tickFrequency() -> ? is
                return True
        elif watering:
            if moistureRange[1] < soilMoistureSensorFloat:
                self.watering = False
            else:
                wateringSolenoid.open(tickFrequency())
        else:
            # otherwise it is fine :)!
            return False
