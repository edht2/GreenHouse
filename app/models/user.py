from app.extensions import db

class User(db.Model):
    id              = db.Column(db.Integer,     primary_key = True )
    first_name      = db.Column(db.String(50),  nullable    = False)
    last_name       = db.Column(db.String(100), nullable    = False)
    email           = db.Column(db.String(100), nullable    = False)
    password        = db.Column(db.String(500), nullable    = False)
    
    def get_id(self):
        # this is required by flask_login!
        return self.id