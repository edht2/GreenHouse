from app.extensions import db

class GreenHouse(db.Model):
    id              = db.Column(db.Integer,     primary_key = True )
    climate         = db.Column(db.String(1),   nullable    = False)
    temp            = db.Column(db.Integer,     nullable    = False)