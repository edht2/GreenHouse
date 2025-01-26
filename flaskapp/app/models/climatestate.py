from app.extensions import db
from datetime import datetime as dt
from app.app_extensions.log import log

class ClimateState(db.Model):
    __tablename__ = 'climateState'
    id          = db.Column(db.Integer,     primary_key = True )
    climate     = db.Column(db.Integer,     nullable    = False)
    temp        = db.Column(db.Integer,     nullable    = False) # Temperature in °C
    rh          = db.Column(db.Integer,     nullable    = False) # Relitive Humidity
    co2_ppm     = db.Column(db.Integer,     nullable    = False) # CO2 ppm (Parts per million)
    ap_hPa      = db.Column(db.Integer,     nullable    = False) # Atmospheric pressure in hPa (hectopascal)
    beds        = db.relationship("Bed", backref="bed", lazy=True)
    time_stamp  = db.Column(db.DateTime,    default     = dt.now()) # When were these readings taken?
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' succesfully created")
    
    def co2_percent(self):
        co2_percentage = self.co2_ppm / 1000000 # this is a float (0-1)
        co2_percentage *= 100 # this is a percentage
        return co2_percentage