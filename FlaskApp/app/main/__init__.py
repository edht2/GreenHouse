from flask import Blueprint

# ***** Creating the blueprints! *****
main = Blueprint('main', __name__)
from app.main.routes import main as m
""" accessable to everyone """
