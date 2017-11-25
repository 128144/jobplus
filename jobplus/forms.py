from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db, User
from flask import flash

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first(): 
            raise ValidationError('邮箱未注册') 
    
    def validate_password(self, field): 
        user = User.query.filter_by(email=self.email.data).first() 
        if user and not user.check_password(field.data): 
            raise ValidationError('密码错误')



