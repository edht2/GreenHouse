from app.sensors.SCD30.scd30 import SCD30 as SCD30sen
from app.bed import Bed

def instantiate_sensorpi(data):
    beds = [
        Bed(
            chirpSensorI2CAddress=bed["chirpSensorI2CAddress"],
            chirpSensorCalibration=bed['chirpSensorCalibration'],
            bedNumber=bed['bedNumber'])
        for bed in data['beds']]
    # populate beds with a list of 'Bed' objects    
        
    SCD30 = SCD30sen()
    # this is the RH%, CO², temperature sensor it requires no parameters!
    return beds, SCD30