from app.extensions.utils import utils
from app.main.conf import sensorSendFrequency
from time import sleep

class SM:
    def __init__(self):
        """ SM class is a watering method - the default one (also the best).
        This reads the soil's moisture content and waters it accoringly, very simple! """
        pass
    
    def tick(self, bed):
        if bed.moistureRange[0] > bed.soilMoistureSensorFloat:
            # i.e not enough water
            self.waterUntilSatisfied()
            return
        else:
            # otherwise it is fine :)!
            return False
    
    @utils.fire_and_forget   
    def waterUntilSatisfied(self, bed):
        """ The way that the SM watering method works: the programme opens the watering value.
        The irregation systen takes ~10 minutes to water the plant. And every 10 seconds new
        watering data is shared with the app. So every 10 seconds we validate the water consentrate
        relitive to the max amount of water wanted. """
        sufficientlyWatered = False
        
        bed.ws.open()
        while not sufficientlyWatered:
            if bed.soilMoistureSensorFloat >= bed.moistureRange:
                sufficientlyWatered = True
                # ok time to stop watering :)
            else:
                # otherwise we can just wait
                sleep(10)
                # I wait 10 seconds as every 10 all of the sensor values are updated
            