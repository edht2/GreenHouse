from app.app_extensions.log import log
from app.models import User
from app.extensions import db


def populate_users():
    """ Populate the user table so that we can test the system more easily """
    
    try:
        ed = User(first_name="Ed", last_name="Haig-Thomas", email="ehaigthomas@gmail.com", password="gerbil", role="admin")
        ed.hash_password()
        db.session.add(ed)
        db.session.commit()
        log(True, 'var', 'populate_users', 'populated user table')
    except Exception as error:
        log(False, 'var', 'populate_users', 'Failed to populate the user table!', error=error)
