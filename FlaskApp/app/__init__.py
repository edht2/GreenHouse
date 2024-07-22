from os import system
from app.app_extensions.log import log
system('clear')
log(None, '', '', 'Setting up app object...', abort=False)

from flask import Flask
from app.extensions import db, fl
from flask_login import current_user
from datetime import date, timedelta
from app.app_extensions.calendar import populate_calendar
from colorama import Fore, Style
from random import randint, choice
from config import Config
from app.models import *
from time import sleep
import logging

def create_app(config_class=Config):
    """ This is the Flask App Factory. This function creates and builds the app obj. """
    
    try:
        app = Flask(__name__)
        app.config.from_object(config_class)

        # ***** Database *****
        db.init_app(app)
        # ********************
        
        # ***** Flask Login *****
        fl.init_app(app)
        fl.login_view = "main.login"
        @fl.user_loader
        def load_user(user_id): 
            return User.query.get(int(user_id))
        # ***********************
        
        # ***** Register Blueprints *****
        from app.main import main
        app.register_blueprint(main)
        log(True, 'flaskapp', 'main', "Registered the 'main' blueprint")
        
        from app.admin import admin
        app.register_blueprint(admin)
        log(True, 'flaskapp', 'admin', "Registered the 'admin' blueprint")
        
        from app.error import error
        app.register_blueprint(error)
        log(True, 'flaskapp', 'error', "Registered the 'error' blueprint")
        # ***********************
        
        with app.app_context():
            lg = logging.getLogger('werkzeug')
            lg.setLevel(logging.ERROR)
            
            db.drop_all()
            # deletes the DB
            db.create_all()
            # recreates the DB
            # I do this so the DB auto refreshed without me doing anything
            
            # ***** Populate Calendar *****
            populate_calendar()
            # *****************************
        
            ed = User(full_name="Ed Haig-Thomas", email="ehaigthomas@gmail.com", password="gerbil", permissions=1)
            ed.hash_password()
            db.session.add(ed)
            db.session.commit()
            
            log(True, 'flaskapp', 'initialisation', f'Flask app build successfuly created')
            log('Done', '', '', 'App is live at', arg=f'http://192.168.1.104:5000/', abort=False)
    except Exception as error:
        log(False, 'flaskapp', 'initialisation', f'Failed to built app object!', error=error, abort=True)

    # return constructed app object!
    return app