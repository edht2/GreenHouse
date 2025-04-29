import jwt
from flask import request, jsonify, g
from functools import wraps
from datetime import datetime, timedelta, timezone
from config import Config
from app.models import User
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Let Flask-JWT-Extended handle both JWT and CSRF verification
            verify_jwt_in_request(locations=['cookies'])
            current_user_id = get_jwt_identity()
            user = User.query.get(current_user_id)
            if not user:
                return jsonify({'message': 'Invalid token - user not found'}), 401
            g.current_user = user
        except Exception as e:
            return jsonify({'message': 'Invalid or missing token'}), 401

        return f(*args, **kwargs)

    return decorated_function