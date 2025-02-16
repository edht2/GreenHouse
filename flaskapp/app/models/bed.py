from app.extensions import db
from app.app_extensions.log import log
from datetime import datetime as dt

class Bed(db.Model):
    __tablename__ = 'Bed'
    id          = db.Column(db.Integer,     primary_key = True )
    bed_name      = db.Column(db.String,    nullable    = False) 
    sm_percent  = db.Column(db.Integer,     nullable    = False) # Soil moisture %
    cz_name       = db.Column(db.String,    nullable    = False) # to which climate zone does it refer#
    time_stamp  = db.Column(db.DateTime,    default     = dt.now(), nullable = False) # When were these readings taken?
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' successfully created")
