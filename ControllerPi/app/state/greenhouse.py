from app.main.bed import Bed
from app.main.ClimateZone import ClimateZone
from app.controll.solenoid import Solenoid
from app.controll.acctuator import Acctuator
from app.wateringMethods.soilmoisture import SM
from app.extensions.log import log
from app.extensions.mqtt import pub, sub
from json import loads

setupJSONstring = open("app/state/state.json").read()
setupDict = loads(setupJSONstring)

greenhouse = []
# greenhouse[0].beds[0].wateringMethod.soilMoistureFloat = new data

for climateZone in setupDict['climateZones']:
    # for each climate zone

    beds = []
    sideWindowAcctuators = []
    topWindowAcctuators = []

    for bed in climateZone['Beds']:
        # for each bed
        beds.append(Bed(
            wateringMethod=SM(targetMoistureRange=bed['bedMoistureRange']),
            wateringSolenoid=Solenoid(bed['wateringSolenoidRelayIndex']),
            climateZoneNumber=climateZone['climateZoneNumber'],
            bedNumber=bed['bedNumber'])
            ) # make a bed object
        
    for swin in climateZone['sideWindows']:
        # for every side window!
        sideWindowAcctuators.append(Acctuator(
            relayIndexes=[swin['acctuatorRelayIndexExtend'], swin['acctuatorRelayIndexRetract']],
            extensionTime=60))
        
    for twin in climateZone['topWindows']:
        # for every top window!
        topWindowAcctuators.append(Acctuator(
            relayIndexes=[twin['acctuatorRelayIndexExtend'], twin['acctuatorRelayIndexRetract']],
            extensionTime=60))
    
    greenhouse.append(ClimateZone(
        beds=beds,
        topWindows=topWindowAcctuators,
        sideWindows=sideWindowAcctuators,
        heatingSolenoid=climateZone['heatingSolenoidRelayIndex'],
        mistingSolenoid=climateZone['mistingSolenoidRelayIndex'],
        climateZoneNumber=climateZone['climateZoneNumber'],
        extremeTemperatureRange=climateZone['extremeTemperatureRange'],
        relativeHumidityRange=climateZone['targetHumidity%'],
        co2ppmMin=climateZone['minimumTargetCO2%']))
    
def onConfigRequest(data:str):
    # the request will look something like "climateZone : 1"
    try:
        climateZoneNumber = int(data.split(':')[1].strip())
        # the climate zone number has been extracted!
        
        # now I must turn all of the bed objects into a string parsable json!
        bed_list = []
        for bed in beds:
            bed_dict = {
                "chirpSensorI2CAddress" : bed.
                "chirpSensorCalibration"
                "wateringSolenoidRelayIndex"
                "bedMoistureRange"
                "bedNumber"
            }


        pub.publish()

    except error as e:
        log('ControllerPi', False, 'configuration', 'mqtt', 'Incompatible format request message: ', arg=data, error=e)