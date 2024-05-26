from flask import Blueprint

admin = Blueprint('admin', __name__)
from app.admin.routes import admin as a
""" only accessable to admins """
