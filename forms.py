from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired()])
	last_name = StringField('Last name', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(),Email('Please enter valid mail')])
	password = PasswordField('Password', validators=[DataRequired(),Length(min=6, message='Password must be 6 chars or more')])
	submit = SubmitField('Sign up')