from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..models import User 

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    username = StringField( 'Username', validators = [DataRequired(), Length(min = 3, max = 18)] )
    email = StringField( 'Email', validators = [DataRequired(), Email()] )
    password = PasswordField( 'Password', validators = [DataRequired()] )
    confirm_password = PasswordField( 'Confirm Password', validators = [DataRequired(), EqualTo('password')] )
    submit = SubmitField('Signup')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('An account with that email already exists')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')