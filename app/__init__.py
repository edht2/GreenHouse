from flask import Flask, render_template
from app.extensions import db
from config import Config
from app import models

def create_app(config_class=Config):
    """ This is the Flask App Factory. This function creates and builds the app obj. """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # ***** Database *****
    db.init_app(app)
    
    with app.app_context():
        db.drop_all() # deletes the DB
        db.create_all() # recreates the DB
        # I do this so the DB auto refreshed without me doing anything


    # ***** Register Blueprints *****
    from app.main import main
    app.register_blueprint(main)
    
    from app.admin import admin
    app.register_blueprint(admin)
    
    from app.error import error
    app.register_blueprint(error)

    # return app object!
    return app

