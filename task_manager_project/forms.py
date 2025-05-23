from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
    ad = StringField("Ad", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Parola", validators=[DataRequired()])
    confirm = PasswordField("Parola Tekrar", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Kayıt Ol")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Parola", validators=[DataRequired()])
    submit = SubmitField("Giriş Yap")

class TaskForm(FlaskForm):
    title = StringField("Başlık", validators=[DataRequired()])
    description = TextAreaField("Açıklama")
    due_date = DateField("Teslim Tarihi", format="%Y-%m-%d")
    submit = SubmitField("Kaydet")
