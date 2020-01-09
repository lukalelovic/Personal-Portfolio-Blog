from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    title = StringField('Enter Post Title:', validators=[DataRequired()])
    post = TextAreaField('Enter Post Body:', validators=[DataRequired()])
    submit = SubmitField('Submit')

#class ContactForm(FlaskForm):
    #name = StringField('Your Name*', validators=[DataRequired()])
    #email = StringField('Your Email*',validators=[DataRequired()])
    #subject = StringField('Your Subject...')
    #message = TextAreaField('Your message...')
    #submit = SubmitField('Submit')
