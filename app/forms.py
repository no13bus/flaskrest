from flask_wtf import Form
from wtforms import PasswordField, SubmitField, TextField

class LoginForm(Form):
    username = TextField('username')
    password = PasswordField('password')
    submit = SubmitField('Login')