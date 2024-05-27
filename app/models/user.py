from app.extensions import db
from passlib.hash import sha256_crypt

class User(db.Model):
    """ The 'User' table will be used for storing the users. (Big shocker :O)
    These users would be like the Gardeners or Owner """
    id          = db.Column(db.Integer,     primary_key = True )
    full_name   = db.Column(db.String(100), nullable    = False)
    email       = db.Column(db.String(100), nullable    = False)
    password    = db.Column(db.String(500), nullable    = False)
    permissions = db.Column(db.Integer,     nullable    = False)
    # permissions will show if the user is a gardener or admin
    
    def hash_password(self):
        self.password = sha256_crypt.hash(self.password)
        # encrpt the password for security
        
    def validate_password(self, attempt):
        sha256_crypt.verify()
    
    def get_id(self):
        # this is required by flask_login
        return self.id