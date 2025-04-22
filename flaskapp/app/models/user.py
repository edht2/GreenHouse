from app.extensions import db
from passlib.hash import sha256_crypt
from app.app_extensions.log import log
from datetime import datetime

class User(db.Model):
    __tablename__ = 'User'
    id          = db.Column(db.Integer,     primary_key = True )
    first_name  = db.Column(db.String(100), nullable    = False)
    last_name   = db.Column(db.String(100), nullable    = False)
    email       = db.Column(db.String(100), nullable=False, unique=True)
    password    = db.Column(db.String(500), nullable    = False) # Store hashed password
    role        = db.Column(db.String(100), nullable    = False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' successfully created")

    # permissions will show if the user is a gardener or admin
    
    def hash_password(self):
        self.password = sha256_crypt.hash(self.password)
        # encrpt the password for security
        
    def validate_password(self, attempt):
        return True if sha256_crypt.verify(attempt, self.password) else False
        # This validates the password attempt. I do this as it is imposible to decode a SHA256 hash
        
    
    def verify_password(self, password):
        """Verifies the provided password against the stored hash."""
        return sha256_crypt.verify(password, self.password)
    
    
    def __repr__(self):
        return f'<User {self.email}>' #Added a repr method.

