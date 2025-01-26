from app.extensions import db
from app.app_extensions.log import log

class Bed(db.Model):
    __tablename__ = 'Bed'
    id          = db.Column(db.Integer,     primary_key = True )
    bed_id      = db.Column(db.Integer,     nullable    = False) # Bed id
    sm_percent  = db.Column(db.Integer,     nullable    = False) # Soil moisture %
    cs_id       = db.Column(db.Integer,     db.ForeignKey('climateState.id'), nullable=False) # Climate reading id#
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' succesfully created")