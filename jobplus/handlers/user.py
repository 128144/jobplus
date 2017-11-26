from flask import Blueprint, render_template, flash
from jobplus.forms import UserprofileForm
from jobplus.models import db, User
from flask_login import login_user, logout_user, login_required


user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UserprofileForm()
    return render_template('user/profile.html', form=form)
