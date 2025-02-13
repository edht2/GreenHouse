
from app.extensions import db, datetime
from app.app_extensions.log import log

class EnvLimits(db.Model):
    __tablename__ = 'EnvLimits'
    id              = db.Column(db.Integer,  primary_key = True )
    cz1_temp_low    = db.Column(db.Integer,  nullable    = False)
    cz1_temp_high   = db.Column(db.Integer,  nullable    = False)
    cz1_rh_low      = db.Column(db.Integer,  nullable    = False)
    cz1_rh_high     = db.Column(db.Integer,  nullable    = False)
    cz1_bed1_low    = db.Column(db.Integer,  nullable    = False)
    cz1_bed1_high   = db.Column(db.Integer,  nullable    = False)
    cz1_bed2_low    = db.Column(db.Integer,  nullable    = False)
    cz1_bed2_high   = db.Column(db.Integer,  nullable    = False)
    cz1_bed3_low    = db.Column(db.Integer,  nullable    = False)
    cz1_bed3_high   = db.Column(db.Integer,  nullable    = False)
    cz2_temp_low    = db.Column(db.Integer,  nullable    = False) 
    cz2_temp_high   = db.Column(db.Integer,  nullable    = False)
    cz2_rh_low      = db.Column(db.Integer,  nullable    = False)
    cz2_rh_high     = db.Column(db.Integer,  nullable    = False)
    cz2_bed4_low    = db.Column(db.Integer,  nullable    = False)
    cz2_bed4_high   = db.Column(db.Integer,  nullable    = False)
    cz2_bed5_low    = db.Column(db.Integer,  nullable    = False)
    cz2_bed5_high   = db.Column(db.Integer,  nullable    = False)
    cz2_bed6_low    = db.Column(db.Integer,  nullable    = False)
    cz2_bed6_high   = db.Column(db.Integer,  nullable    = False)
    cz2_bed7_low    = db.Column(db.Integer,  nullable    = False)
    cz2_bed7_high   = db.Column(db.Integer,  nullable    = False)
    cz2_bed8_low    = db.Column(db.Integer,  nullable    = False)
    cz2_bed8_high   = db.Column(db.Integer,  nullable    = False)
    date_time  = db.Column(db.DateTime, default     = datetime.now)
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' successfully created")
