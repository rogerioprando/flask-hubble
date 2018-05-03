from flask import render_template, Blueprint, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required, logout_user
from .forms import RegisterForm, LoginForm
from project import db
from project.models import User


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Bem vindo {}' .format(current_user.email), 'success') # tentar mostrar o nome aqui
                return redirect(url_for('core.index'))
            else:
                flash('Erro! Credenciais incorretas.', 'error')
    return render_template('login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    print("USER QUERY: {}".format(user.email))
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Logout efetuado.', 'info')
    return redirect(url_for('users.login'))


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_new_user():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.username.data, form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Usuário registrado', 'success')
                return redirect(url_for('core.index'))
            except IntegrityError:
                db.session.rollback()
                flash('Erro! Email {} já está cadastrado.' .format(form.email.data), 'error')
    return render_template('register.html', form=form)


