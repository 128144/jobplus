from flask import Blueprint, render_template, flash
from jobplus.forms import CompanyprofileForm
from jobplus.models import db, Company
from flask_login import login_user, logout_user, login_required

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    return render_template('company.html')


@company.route('/admin/profile', methods=['GET', 'POST'])
def profile():
    form = CompanyprofileForm()
    return render_template('company/admin/profile.html', form=form)


