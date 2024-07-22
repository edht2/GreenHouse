from app.extensions import db
from passlib.hash import sha256_crypt
from flask_login import UserMixin
from app.app_extensions.log import log

class User(UserMixin, db.Model):
    """ The 'User' table will be used for storing the users. (Big shocker :O)
    These users would be like the Gardeners or Owner """
    __tablename__ = 'User'
    id          = db.Column(db.Integer,     primary_key = True )
    full_name   = db.Column(db.String(100), nullable    = False)
    email       = db.Column(db.String(100), nullable    = False)
    password    = db.Column(db.String(500), nullable    = False)
    permissions = db.Column(db.Integer,     nullable    = False)
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' succesfully created")
    # permissions will show if the user is a gardener or admin
    
    def hash_password(self):
        self.password = sha256_crypt.hash(self.password)
        # encrpt the password for security
        
    def validate_password(self, attempt):
        return True if sha256_crypt.verify(attempt, self.password) else False
        # This validates the password attempt. I do this as it is imposible to decode a SHA256 hash
        
    def get_id(self):
        # this is required by flask_login
        return self.id