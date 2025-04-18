# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, EditProfileForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form, title='Register')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Введены неверные данные')
    return render_template('login.html', form=form, title='Login')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/account')
@login_required
def account():
    return render_template('account.html')

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(
        original_username=current_user.username,
        original_email=current_user.email
    )

    if form.validate_on_submit():
        if not bcrypt.check_password_hash(current_user.password, form.current_password.data):
            flash('Неверный текущий пароль', 'danger')
        else:
            current_user.username = form.username.data
            current_user.email = form.email.data
            if form.new_password.data:
                hashed_pw = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
                current_user.password = hashed_pw
            db.session.commit()
            flash('Профиль обновлён!', 'success')
            return redirect(url_for('main.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('edit_profile.html', form=form, title='Редактирование профиля')
