import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = b"gsddfshdlviuiHJHJHHduyfyify847f7wchri8oJMOMU&rd8FD8wper8fuwp9f8eurgjsdlvud8gusdfigudsfh8g79p8h8rtugjfijdjb"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    