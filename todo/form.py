from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class AddTodoForm(FlaskForm):
    title = StringField(label='Title:', validators=[DataRequired()])
    description = StringField(label='Description:')
    submit = SubmitField(label='Add')