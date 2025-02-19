from app.extensions import db
from app.models import ClimateZone, Bed 


def message_handler(mqtt_message):
    topic = mqtt_message["topic"]
    cz_name = mqtt_message["topic"][:3]
    is_bed = topic.find("bed")

    if is_bed != -1:
        bed_name = "bed" + topic[7]
        data = Bed(bed_name=bed_name, 
        sm_percent=mqtt_message["payload"]["median_soil_moist"], 
        cz_name=cz_name)

    else:
        data = ClimateZone(climate_zone_name = cz_name, 
        rh=mqtt_message["payload"]["median_rh"], 
        temp=mqtt_message["payload"]["median_temp"], 
        co2_ppm=mqtt_message["payload"]["median_co2_ppm"])
    
    db.session.add(data)
    db.session.commit()
    print("sent to database")