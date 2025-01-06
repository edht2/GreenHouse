from app.mqtt.mqtt import sub

def s(msg):
    print(msg)

sub.subscribe("climate_zone_1/bed1", s)