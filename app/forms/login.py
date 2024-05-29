import wtforms as wtf
from app.extensions import db
from app.models import User

class Login(wtf.Form):
    """ This is a really simple form """
    email    = wtf.EmailField('Email')
    password = wtf.PasswordField('Password')
    
    def validate_email(form, field):
        """ Validating the email. I do this so it can tell you if the email entered exists
        OR if they entered anything at all"""
        email = field.data # I re-define the email value
        if field.data != '':
            if not db.session.query(User).filter_by(email=email).first():
                raise wtf.ValidationError("Email not registered.")
        else:
            raise wtf.ValidationError("Please fill this field.")
    
    def validate_password(form, field):
        """ Validating password to match with the email OR if anything was entered into the
        field! Very cool """
        password = field.data
        email = form.email.data
        if field.data != '':
            account = db.session.query(User).filter_by(email=email).first()
            if account:
                if not account.validate_password(password):
                    raise wtf.ValidationError("Email or Password credentails are invalid.")
        else:
            raise wtf.ValidationError("Please fill this field.")