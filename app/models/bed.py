from app.extensions import db

class Bed(db.Model):
    __tablename__ = 'bed'
    id          = db.Column(db.Integer,     primary_key = True )
    bed_id      = db.Column(db.Integer,     nullable    = False) # Bed id
    sm_percent  = db.Column(db.Integer,     nullable    = False) # Soil moisture %
    cs_id       = db.Column(db.Integer,     db.ForeignKey('climateState.id'), nullable=False) # Climate reading id