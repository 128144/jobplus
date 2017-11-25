from flask import Blueprint, render_template, flash
from jobplus.forms import LoginForm
from jobplus.models import db, User
from flask_login import login_user, logout_user, login_required

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first() 
        login_user(user, form.remember_me.data) 
        if user.is_admin:
            return redirect(url_for('#'))
        elif user.is_company:
            return redirect(url_for('#'))
        else:
            return redirect(url_for('#'))
    flash("账号或密码错误", "warning")
    return render_template('login.html', form=form)

@front.route('/logout') 
@login_required 
def logout(): 
    logout_user() 
    flash('您已经退出登陆', 'success') 
    return redirect(url_for('.index'))
