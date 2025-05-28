from app.extensions import db
from app.models import *


env_limits = vars(EnvLimits.query.order_by(EnvLimits.date_time.desc()).first())
