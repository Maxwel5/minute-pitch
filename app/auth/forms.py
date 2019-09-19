from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired,Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(FlaskForm):
    username = StringField( 'Username', validators = [DataRequired(), Length(min = 3, max = 18)] )
    email = StringField( 'Email', validators = [DataRequired(), Email()] )
    password = PasswordField( 'Password', validators = [DataRequired()] )
    confirm_password = PasswordField( 'Confirm Password', validators = [DataRequired(), EqualTo('password')] )