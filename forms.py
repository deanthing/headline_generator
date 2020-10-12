from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional

class Query(FlaskForm):
  headlines = IntegerField("Number of Headlines to Generate", [DataRequired('Input Required/Must be a number')])
  customerName = StringField("Customer Name (Optional)", validators=[Optional('Optional')])
  submitQuery = SubmitField('Submit', validators=[DataRequired()])

class Entry(FlaskForm):
  pswd = StringField("Password*", [DataRequired('Password Required')], render_kw={"placeholder": "Enter Secret Passwort"})
  submitEntry = SubmitField('Submit', validators=[DataRequired()])