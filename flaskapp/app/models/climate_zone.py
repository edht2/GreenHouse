from app.extensions import db
from datetime import datetime as dt
from app.app_extensions.log import log

class ClimateZone(db.Model):
    __tablename__ = 'ClimateZone'
    id          = db.Column(db.Integer,   primary_key = True )
    climate_zone_name = db.Column(db.String, nullable = False)
    temp        = db.Column(db.Float,     nullable    = False) # Temperature in °C
    rh          = db.Column(db.Float,     nullable    = False) # Relitive Humidity
    co2_ppm     = db.Column(db.Float,     nullable    = False) # CO2 ppm (Parts per million)
    ap_hPa      = db.Column(db.Float,     nullable    = True ) # Atmospheric pressure in hPa (hectopascal)
    time_stamp  = db.Column(db.DateTime,    default     = dt.now(), nullable = False) # When were these readings taken?
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' successfully created")
    
    def co2_percent(self):
        co2_percentage = self.co2_ppm / 1000000 # this is a float (0-1)
        co2_percentage *= 100 # this is a percentage
        return co2_percentage

