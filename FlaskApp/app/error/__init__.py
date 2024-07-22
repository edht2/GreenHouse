from flask import Blueprint

error = Blueprint('error', __name__)
from app.error.routes import error as e
""" error handler, like 404 exception """