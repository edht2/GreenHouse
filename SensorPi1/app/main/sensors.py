from app.main.conf import climateZone
from app.state import chirpSensors, SCD30_humco2

def get_sensor_o_dict():
    scd30_data = SCD30_humco2.takeReading()
    csens = []
    for csen in chirpSensors:
        csens.append(csen.takeReading())

    return str({
        'climateZone' : climateZone(),
        'chirpSensors' : {
            str(csens)
        },
        'RH%'   : round(scd30_data[2]),
        'C02%'  : round(scd30_data[0]/10000, 3),
        'C02ppm': round(scd30_data[0]),
        'TEMPC' : round(scd30_data[1], 1)
    })