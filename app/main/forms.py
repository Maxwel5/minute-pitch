from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    category = SelectField(user'Pitch Category', choices=[('bootcamp', 'bootcamp'), ('trip', 'trip'), ('sports', 'sports')])
    pitch = TextAreaField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    pitch = TextAreaField('Comment something',validators = [Required()])
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Describe yourself.',validators = [Required()])
    submit = SubmitField('Submit')