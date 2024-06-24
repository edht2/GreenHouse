from app.extensions import db

class Event(db.Model):
    __tablename__ = 'Event'
    id          = db.Column(db.Integer,     primary_key = True )
    date        = db.Column(db.Integer,     nullable    = False)
    event_title = db.Column(db.String(250), nullable    = False)