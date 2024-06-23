from app.extensions import db

class Event(db.Model):
    __tablename__ = 'Event'
    id          = db.Column(db.Integer,     primary_key = True )
    date_id     = db.Column(db.Integer,     nullable    = False)
    title       = db.Column(db.String(250), nullable    = False)
    
class Date(db.Model):
    __tablename__ = 'Date'
    id          = db.Column(db.Integer,     primary_key = True )
    date        = db.Column(db.Date,        nullable    = False)