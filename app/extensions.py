from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ***** Create DB object *****
db = SQLAlchemy()

# ***** Create FL object *****
fl = LoginManager() # flask login