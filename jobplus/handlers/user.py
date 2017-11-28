from flask import Blueprint, render_template, flash, redirect, url_for
from jobplus.forms import UserprofileForm
from jobplus.models import db, User
from flask_login import login_user, logout_user, login_required


user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UserprofileForm()
    user = User.query.filter_by(email=form.email.data).first()
    form = UserprofileForm(obj=user)
    if form.validate_on_submit(): 
        
        
        form.update_userprofile(user)
        flash('更新配置成功！', 'success')
        return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form=form)


