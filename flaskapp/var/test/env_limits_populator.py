from app.app_extensions.log import log
from app.models import EnvLimits
from app.extensions import db


def populate_env_limits():
    """ Populate the user table so that we can test the system more easily """
    
    try:
        test_data = EnvLimits(
            cz1_temp_low  = 15,
            cz1_temp_high = 25,
            cz1_rh_low    = 45,
            cz1_rh_high   = 65,
            cz1_bed1_low  = 50,
            cz1_bed1_high = 70,
            cz1_bed2_low  = 50,
            cz1_bed2_high = 70,
            cz1_bed3_low  = 50,
            cz1_bed3_high = 70,
            cz2_temp_low  = 22,
            cz2_temp_high = 28,
            cz2_rh_low    = 60,
            cz2_rh_high   = 80,
            cz2_bed4_low  = 50,
            cz2_bed4_high = 70,
            cz2_bed5_low  = 50,
            cz2_bed5_high = 70,
            cz2_bed6_low  = 50,
            cz2_bed6_high = 70,
            cz2_bed7_low  = 50,
            cz2_bed7_high = 70,
            cz2_bed8_low  = 50,
            cz2_bed8_high = 70
        )

        db.session.add(test_data)
        db.session.commit()
        log(True, 'var', 'populate_env_limits', 'populated EnvLimits table')
    except Exception as error:
        log(False, 'var', 'populate_env_limits', 'Failed to populate the EnvLimits table!', error=error)
