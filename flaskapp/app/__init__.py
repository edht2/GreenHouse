from flask import Flask, render_template, request, jsonify, make_response, current_app
from app.extensions import db
from app.main import main
from app.admin import admin
from app.error import error
import logging
from var.test.calendar_populator import populate_calendar
from var.test.user_populator import populate_users
from var.test.env_limits_populator import populate_env_limits
from var.test.sensor_data import *
from app.mqtt import pub, sub
from app.mqtt import message_handler
from app.models import User, EnvLimits
from config import Config
import jwt
from flask_cors import CORS
from app.auth import token_required # Import from auth.py
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt, JWTManager, create_access_token, set_access_cookies, unset_jwt_cookies # Import JWTManager and functions
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError # Import exceptions from jwt
from json import dumps
import logging
import threading




def create_app(config_class=Config):
    """This is the Flask App Factory. Handles app creation and configuration."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://192.168.1.228:8080"}})
    configure_extensions(app)
    register_blueprints(app)
    configure_jwt(app)  # Configure JWT AFTER blueprints
    #create_database(app)
    #populate_database(app)
    configure_mqtt_pub(app)
    configure_mqtt_sub(app)
    return app

def configure_extensions(app):
    """Configures Flask extensions (e.g., database)."""
    db.init_app(app)

def register_blueprints(app):
    """Registers Flask blueprints."""
    app.register_blueprint(main)
    logging.info("Registered the 'main' blueprint")
    app.register_blueprint(admin)
    logging.info("Registered the 'admin' blueprint")
    app.register_blueprint(error)
    logging.info("Registered the 'error' blueprint")

def configure_jwt(app):
    """Configures JWT authentication."""
    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY  # Use your SECRET_KEY from Config
    print('secret key at configuration time...', Config.SECRET_KEY)
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_COOKIE_SECURE"] = False  # Only send over HTTPS in production
    app.config["JWT_COOKIE_SAMESITE"] = "Lax"  # Required for cross-site cookies
    app.config["JWT_COOKIE_CSRF_PROTECT"] = True
    jwt_manager = JWTManager(app)

    
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(password):
            access_token = create_access_token(identity=str(user.id), fresh=True)
            response_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role
            }
            response = jsonify(response_data)
            try:
                print("set_access_cookies called")
                set_access_cookies(response, access_token)
            except Exception as e:
                print(f"Error setting cookies: {e}")
                return jsonify({'message': 'Login successful, but error setting cookies'}), 500
            return response
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

    @app.route('/protected', methods=['GET'])
    @token_required
    def protected():
        user = request.current_user
        return jsonify({'message': f'This is a protected route. Welcome, {user.email}'}), 200

    @app.route('/logout', methods=['POST'])
    def logout():
        response = jsonify({'message': 'Logged out successfully'})
        response.delete_cookie('jwt_token', path='/', samesite='None', secure=True)
        return response, 200
    
    
    @app.route('/verify-token', methods=['POST'])
    def verify_token():
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            current_user = User.query.get(current_user_id)
            if current_user:
                return jsonify({
                    "firstName": current_user.first_name,
                    "lastName": current_user.last_name,
                    "role": current_user.role
                }), 200
            else:
                return jsonify({"msg": "Invalid user"}), 401
        except Exception as e:
            return jsonify({"msg": "Invalid or expired token"}), 401
        
        
    @app.route('/set_test_cookie')
    def set_test_cookie():
        resp = make_response("Setting test cookie")
        resp.set_cookie('test_cookie', 'test_value', path='/')
        return resp



"""def create_database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
        logging.info("Database tables created")"""

"""def populate_database(app):
    with app.app_context():
        populate_calendar()
        populate_users()
        populate_env_limits()
        for i in mqtt_messages:
            message_handler(i)
        logging.info("Database populated with initial data")"""

def configure_mqtt_pub(app):
    """Configures MQTT publishing. This publishes the env limits in the database to be shared with the controller pi"""
    with app.app_context():
        try:
            mqtt_topic = current_app.config.get('MQTT_LIMIT_TOPIC')
            print('mqtt_topic: ', mqtt_topic)
            latest_env_limits_record = vars(
                EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())
            latest_env_limits_record["date_time"] = str(latest_env_limits_record["date_time"])
            latest_env_limits_record["_sa_instance_state"] = str(
                latest_env_limits_record["_sa_instance_state"])

            json_string = dumps(latest_env_limits_record)
            print(json_string)
            pub.publish(mqtt_topic, json_string)
            print("we are publishing our env limits")
            logging.info("MQTT publishing configured")
        except Exception as e:
            logging.error(f"Error publishing to MQTT: {e}")

def configure_mqtt_sub(app):
    with app.app_context():
        try:
            mqtt_broker = current_app.config.get('MQTT_BROKER_ADDRESS')
            mqtt_port = current_app.config.get('MQTT_PORT')
            mqtt_topics = current_app.config.get('MQTT_SENSOR_TOPIC')
            if not mqtt_broker or not mqtt_port or not mqtt_topics:
                logging.error("MQTT broker address, port, or topic not configured.")
                return
                        
            subscribe_instance = sub.Subscribe(mqtt_broker, mqtt_port, mqtt_topics, message_handler, app=app) # Pass the 'app' instance
            thread = threading.Thread(target=subscribe_instance.run, daemon=True)
            thread.start()
            print(f"Subscribed to {mqtt_topics} in a separate thread.")

        except Exception as e:
            logging.error(f"Error configuring MQTT subscription: {e}")


if __name__ == "__main__":
    app = create_app()
    logging.info('Flask app started')
    app.run(host='0.0.0.0', port=5000, debug=True)

