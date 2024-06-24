from flask import Flask
from app.extensions import db, fl
from flask_login import current_user
from datetime import date, timedelta
from random import randint
from config import Config
from app.models import *

def create_app(config_class=Config):
    """ This is the Flask App Factory. This function creates and builds the app obj. """
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
    
    from app.admin import admin
    app.register_blueprint(admin)
    
    from app.error import error
    app.register_blueprint(error)
    
    
    with app.app_context():
        # ********************************************
        # THIS IS TO BE DELETED IN A LIVE ENVIRONMENT!
        # ********************************************
        db.drop_all()
        # deletes the DB
        db.create_all()
        # recreates the DB
        
        # I do this so the DB auto refreshed without me doing anything
        ed = User(full_name="Ed Haig-Thomas", email="ehaigthomas@gmail.com", password="gerbil", permissions=1)
        ed.hash_password()
        al = User(full_name="Al Haig-Thomas", email="alhaigthomas@gmail.com", password="gerbil", permissions=1)
        al.hash_password()
        
        tdy = date.today() - timedelta(days=5)
        for i in range(20):
            new_event = Event(date=tdy+timedelta(days=randint(1, 10)), event_title="gerbil wedding")
            db.session.add(new_event)
            
        db.session.add(ed)
        db.session.add(al)
        db.session.commit()

    # return constructed app object!
    return app