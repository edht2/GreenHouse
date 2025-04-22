import jwt
from flask import request, jsonify, g
from functools import wraps
from datetime import datetime, timedelta, timezone
from config import Config
from app.models import User
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity # Import from flask_jwt_extended

def create_jwt(user_id):
    """Generates a JWT for the given user ID."""
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(hours=24)
    }
    print("secret key", Config.SECRET_KEY)
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('jwt_token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # Use flask_jwt_extended's verify_jwt_in_request
            verify_jwt_in_request(locations=['cookies'])  
            user_id = get_jwt_identity() # Use get_jwt_identity
            user = User.query.get(user_id)
            if not user:
                return jsonify({'message': 'Invalid token - user not found'}), 401
            g.current_user = user # Store user in g
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        except Exception as e:
            return jsonify({'message': 'An error occurred', 'error': str(e)}), 401

        return f(*args, **kwargs)

    return decorated_function