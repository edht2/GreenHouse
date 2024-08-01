from app.main.conf import climateZone
from app.state import chirpSensors, Humidity

def get_sensor_o_json():
    pass

def get_sensor_o_dict():
    return {
        'climateZone' : climateZone(),
        'chirpSensors' : {
            'sen1' : {
                'acc' : 300,
                'float' : 70
                # ~70% water detected
            },
            'sen2' : {
                'acc' : 290,
                'float' : 60
            },
            'sen3' : {
                'acc' : 320,
                'float' : 96
            }
        },
        'RH%' : 65,
        'C02%': 0.2,
        'TEMPC' : 21
    }