import wtforms as wtf
from wtforms.validators import DataRequired, NumberRange
from app.extensions import db
from app.models import EnvLimits




    # create dictionary from the EnvLimits table


class Env_limits(wtf.Form):


    cz1_temp_low    = wtf.IntegerField('cz1 temp', validators=[DataRequired(), NumberRange(min=0, max=40, message="Please enter a non-negative number")])
    cz1_temp_high   = wtf.IntegerField('cz1 temp high', validators=[DataRequired(), NumberRange(min=0, max=40, message="Please enter a non-negative number")])
    cz1_rh_low      = wtf.IntegerField('cz1 rh', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_rh_high   = wtf.IntegerField('cz1 rh high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed1_low   = wtf.IntegerField('cz1 bed1', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed1_high   = wtf.IntegerField('cz1 bed1 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed2_low   = wtf.IntegerField('cz1 bed2', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed2_high   = wtf.IntegerField('cz1 bed2 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed3_low   = wtf.IntegerField('cz1 bed3', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz1_bed3_high   = wtf.IntegerField('cz1 bed3 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    
    cz2_temp_low    = wtf.IntegerField('cz2 temp', validators=[DataRequired(), NumberRange(min=0, max=40, message="Please enter a non-negative number")])
    cz2_temp_high   = wtf.IntegerField('cz2 temp high', validators=[DataRequired(), NumberRange(min=0, max=40, message="Please enter a non-negative number")])
    cz2_rh_low      = wtf.IntegerField('cz2 rh', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_rh_high   = wtf.IntegerField('cz2 rh high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed4_low   = wtf.IntegerField('cz2 bed4', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed4_high   = wtf.IntegerField('cz2 bed4 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed5_low   = wtf.IntegerField('cz2 bed5', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed5_high   = wtf.IntegerField('cz2 bed5 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed6_low   = wtf.IntegerField('cz2 bed6', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed6_high   = wtf.IntegerField('cz2 bed6 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed7_low   = wtf.IntegerField('cz2 bed7', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed7_high   = wtf.IntegerField('cz2 bed7 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed8_low   = wtf.IntegerField('cz2 bed8', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    cz2_bed8_high   = wtf.IntegerField('cz2 bed8 high', validators=[DataRequired(), NumberRange(min=0, max=100, message="Please enter a non-negative number")])
    submit = wtf.SubmitField("Submit")

    def __init__(self, limits, *args, **kwargs):
        super(Env_limits, self).__init__(*args, **kwargs)
        self.search_defaults(limits)
    
    def search_defaults(self, limits):
        try:
            defaults = limits

            if defaults:
                self.cz1_temp_low.data = defaults['cz1_temp_low']  if defaults ['cz1_temp_low'] is not None else 'NA'
                self.cz1_temp_high.data = defaults['cz1_temp_high'] if defaults['cz1_temp_high'] is not None else 'NA' 
                self.cz1_rh_low.data = defaults['cz1_rh_low'] if defaults['cz1_rh_low'] is not None else 'NA'
                self.cz1_rh_high.data = defaults['cz1_rh_high'] if defaults['cz1_rh_high'] is not None else 'NA'
                self.cz1_bed1_low.data = defaults['cz1_bed1_low'] if defaults['cz1_bed1_low'] is not None else 'NA'
                self.cz1_bed1_high.data = defaults['cz1_bed1_high'] if defaults['cz1_bed1_high'] is not None else 'NA'
                self.cz1_bed2_low.data = defaults['cz1_bed2_low'] if defaults['cz1_bed2_low'] is not None else 'NA'
                self.cz1_bed2_high.data = defaults['cz1_bed2_high'] if defaults['cz1_bed2_high'] is not None else 'NA' 
                self.cz1_bed3_low.data = defaults['cz1_bed3_low'] if defaults['cz1_bed3_low'] is not None else 'NA'
                self.cz1_bed3_high.data = defaults['cz1_bed3_high'] if defaults['cz1_bed3_high'] is not None else 'NA'

                self.cz2_temp_low.data = defaults['cz2_temp_low']  if defaults ['cz2_temp_low'] is not None else 'NA'
                self.cz2_temp_high.data = defaults['cz2_temp_high'] if defaults['cz2_temp_high'] is not None else 'NA' 
                self.cz2_rh_low.data = defaults['cz2_rh_low'] if defaults['cz2_rh_low'] is not None else 'NA'
                self.cz2_rh_high.data = defaults['cz2_rh_high'] if defaults['cz2_rh_high'] is not None else 'NA'
                self.cz2_bed4_low.data = defaults['cz2_bed4_low'] if defaults['cz2_bed4_low'] is not None else 'NA'
                self.cz2_bed4_high.data = defaults['cz2_bed4_high'] if defaults['cz2_bed4_high'] is not None else 'NA'
                self.cz2_bed5_low.data = defaults['cz2_bed5_low'] if defaults['cz2_bed5_low'] is not None else 'NA'
                self.cz2_bed5_high.data = defaults['cz2_bed5_high'] if defaults['cz2_bed5_high'] is not None else 'NA' 
                self.cz2_bed6_low.data = defaults['cz2_bed6_low'] if defaults['cz2_bed6_low'] is not None else 'NA'
                self.cz2_bed6_high.data = defaults['cz2_bed6_high'] if defaults['cz2_bed6_high'] is not None else 'NA'
                self.cz2_bed7_low.data = defaults['cz2_bed7_low'] if defaults['cz2_bed7_low'] is not None else 'NA'
                self.cz2_bed7_high.data = defaults['cz2_bed7_high'] if defaults['cz2_bed7_high'] is not None else 'NA'
                self.cz2_bed8_low.data = defaults['cz2_bed8_low'] if defaults['cz2_bed8_low'] is not None else 'NA'
                self.cz2_bed8_high.data = defaults['cz2_bed8_high'] if defaults['cz2_bed8_high'] is not None else 'NA'


        except Exception as e:
            # Handle database errors appropriately, e.g., logging or displaying a message
            print(f"Error fetching defaults: {e}")
            # Optionally set default values if database retrieval fails

    
    