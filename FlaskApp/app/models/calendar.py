from app.extensions import db
from app.app_extensions.log import log

class Event(db.Model):
    __tablename__ = 'Event'
    id          = db.Column(db.Integer,     primary_key = True )
    date        = db.Column(db.Integer,     nullable    = False)
    event_title = db.Column(db.String(250), nullable    = False)
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' succesfully created")