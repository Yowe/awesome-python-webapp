from flask import render_template, redirect, request, url_for, flash
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required,logout_user, current_user
from app import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或密码有误')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('您已经可以登录')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你应经退出系统')
    return redirect(url_for('main.index'))



@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed and request.endpoint[:5] != '.auth':
            return redirect(url_for('auth.unconfirmed'))
