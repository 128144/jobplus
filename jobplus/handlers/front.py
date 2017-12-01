from flask import Blueprint, render_template, flash, redirect, url_for
from jobplus.forms import LoginForm, CompanyregisterForm, UserregisterForm
from jobplus.models import db, User
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/companyregister', methods=['GET', 'POST'])
def company_register():
    form = CompanyregisterForm()
    if form.validate_on_submit(): 
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    
    return render_template('company_register.html',form=form)
    
@front.route('/userregister', methods=['GET', 'POST'])
def user_register():
    form = UserregisterForm()
    if form.validate_on_submit(): 
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))

    return render_template('user_register.html',form=form)    

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first() 
        login_user(user, form.remember_me.data) 
        if user.is_admin:
            return redirect(url_for('#'))
        elif user.is_company:
            return redirect(url_for('company.profile'))
        else:
            return redirect(url_for('user.profile'))
        
    

    return render_template('login.html', form=form)

@front.route('/logout') 
@login_required 
def logout(): 
    logout_user() 
    flash('您已经退出登陆', 'success') 
    return redirect(url_for('.index'))
