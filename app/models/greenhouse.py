from app.extensions import db

class GreenHouse(db.Model):
    id          = db.Column(db.Integer,     primary_key = True )
    climate     = db.Column(db.Integer,   nullable    = False)
    # Defines what room in the green house this data is relevent to
    temp        = db.Column(db.Integer,     nullable    = False) # Temperature in °C
    rh          = db.Column(db.Integer,     nullable    = False) # Relitive Humidity
    co2_ppm     = db.Column(db.Integer,     nullable    = False) # CO2 ppm (Parts per million)
    
    def CO2_percent(self):
        co2_percentage = self.co2_ppm / 1000000 # this is a float (0-1)
        co2_percentage *= 100 # this is a percentage
        return co2_percentage
        