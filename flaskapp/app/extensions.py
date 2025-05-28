from flask_sqlalchemy import SQLAlchemy
from app.app_extensions.log import log
from datetime import datetime

# ***** Create DB object *****
try:
    db = SQLAlchemy()
    log(True, 'database', 'initialisation', 'Created database object')
except Exception as error:
    log(False, 'database', 'initialisation', 'Datebase object failed to initialise', error=error)

# ***** Create FL object *****
