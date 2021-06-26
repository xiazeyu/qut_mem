from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from ..models import User
from flask_login import login_user, login_required, logout_user
from .. import db
bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(username=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            next = request.args.get('next')
            return redirect(next or url_for('main.content.list_items'))
        else:
            flash(error)
    return render_template('user/login.html', form=login_form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    email_id = request.args.get('email_id', None)
    contact_number = request.args.get('contact_number', None)
    address = request.args.get('address', None)

    return render_template('user/register.html')

    form = RegisterForm()
    if form.validate_on_submit():
        print('Register form submitted')

        # get username, password and email from the form
        uname = form.username.data
        pwd = form.password.data
        email = form.email.data

        # create password hash
        pwd_hash = generate_password_hash(pwd)

        # create a new user model object
        new_user = User(name=uname, password_hash=pwd_hash, emailid=email)
        db.session.add(new_user)
        db.session.commit()
        # commit to the database and redirect to HTML page
        return redirect(url_for('auth.register'))


@bp.route('/logout')
def logout():
    logout_user()
    return 'Successfully logged out user'
