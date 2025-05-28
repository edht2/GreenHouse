from app.extensions import db
from app.models import ClimateZone, Bed
from flask import current_app
from datetime import datetime as dt
from datetime import timezone

def message_handler(mqtt_message):
    topic = mqtt_message["topic"]
    print('topic',topic)
    cz_name = mqtt_message["topic"][:14]
    is_bed = topic.find("bed")

    try:
        with current_app.app_context():
            timestamp = dt.now(timezone.utc)  # Generate timestamp *now*
            if is_bed != -1:
                bed_name = "bed" + topic[18]
                data = Bed(
                    bed_name=bed_name,
                    sm_percent=mqtt_message["payload"].get("median_soil_moist"),
                    cz_name=cz_name,
                    time_stamp=timestamp
                )
            else:
                data = ClimateZone(
                    climate_zone_name=cz_name,
                    rh=mqtt_message["payload"].get("median_rh"),
                    temp=mqtt_message["payload"].get("median_temp"),
                    co2_ppm=mqtt_message["payload"].get("median_co2_ppm"),
                    time_stamp=timestamp
                )

            db.session.add(data)
            db.session.commit()
            print(f"Processed and saved message for topic: {topic}")

    except Exception as e:
        print(f"Error processing message for topic '{topic}': {e}")
        with current_app.app_context():
            db.session.rollback()  # Rollback in case of error
  