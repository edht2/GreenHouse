from app.extensions import db
from datetime import datetime as dt
from app.app_extensions.log import log

class Todo(db.Model):
    __tablename__ = 'Todo'
    id              = db.Column(db.Integer,     primary_key = True )
    title           = db.Column(db.Integer,     nullable    = False)
    description     = db.Column(db.Text,        nullable    = True )
    #location        = db.Column(db.String(250), nullable    = True )
    image_directory = db.Column(db.String(250), nullable    = True )
    # what three words address!
    is_completed    = db.Column(db.Boolean,     nullable    = False)
    completion_date = db.Column(db.DateTime,    nullable    = True )
    creation_date   = db.Column(db.DateTime,    default = dt.now() )
    log(True, 'database', f'tbl_{__tablename__}', f"Table '{__tablename__}' succesfully created")
    
    def completed(self):
        self.completion_date = dt.now()
        self.is_completed = True
        # set the current date time to the completed date variable