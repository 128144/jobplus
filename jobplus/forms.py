from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, FloatField, TextAreaField
from wtforms.validators import Length, Email, EqualTo, Required, URL
from jobplus.models import db, User, Company
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
    name = StringField('姓名', validators=[Required()])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    tel = StringField('手机号', validators=[Required(), Length(11)])
    working_life = FloatField('工作年限', validators=[Required()])
    upload_resume_url = StringField('简历链接', validators=[Required(), URL])
    submit = SubmitField('提交')

    def update_userprofile(self, userprofile):
        self.populate_obj(userprofile)
        db.session.add(userprofile)
        db.session.commit()
        
        return userprofile


class CompanyprofileForm(FlaskForm):
    name = StringField('企业名称', validators=[Required()])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    logo = StringField('logo图片链接', validators=[Required(), URL])
    site = StringField('网站链接', validators=[Required(), URL])
    description = StringField('一句话简介', validators=[Required(), Length(6,24)])
    about = TextAreaField('详细介绍', validators=[Required()])
    submit = SubmitField('提交')

    def create_companyprofile(self): 
        company = Company()
        self.populate_obj(company)
        db.session.add(company)
        db.session.commit()
        
        return company
