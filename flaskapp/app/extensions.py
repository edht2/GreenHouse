from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.app_extensions.log import log

# ***** Create DB object *****
try:
    db = SQLAlchemy()
    log(True, 'database', 'initialisation', 'Created database object')
except Exception as error:
    log(False, 'database', 'initialisation', 'Datebase object failed to initialise', error=error)

# ***** Create FL object *****
try:
    fl = LoginManager() # flask login
    log(True, 'flasklogin', 'initialisation', 'Created flask-login object')
except Exception as error:
    log(False, 'flasklogin', 'initialisation', 'flask-login object failed to initialise', error=error)