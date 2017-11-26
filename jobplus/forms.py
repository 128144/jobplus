from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, FloatField
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


class UserprofileForm(FlaskForm):
    name = StringField('姓名', validators=[Required(), Length(6,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    tel = StringField('手机号', validators=[Required(), Length(6,24)])
    working_life = FloatField('工作年限', validators=[Required(), Length(6,24)])
    
    submit = SubmitField('提交')


class CompanyprofileForm(FlaskForm):
    name = StringField('企业名称', validators=[Required(), Length(6,24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    logo = StringField('logo图片链接', validators=[Required(), Length(6,100)])
    site = StringField('网站链接', validators=[Required(), Length(6,100)])
    description = StringField('一句话简介', validators=[Required(), Length(6,24)])
    about = StringField('详细介绍', validators=[Required(), Length(6,1024)])

    
    submit = SubmitField('提交')
