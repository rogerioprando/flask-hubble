from flask import render_template, Blueprint, request, url_for, flash, redirect
from project.models import User
from .forms import *
from project import db
from sqlalchemy.exc import IntegrityError

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login')
def login():
    return render_template('login.html')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_new_user():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.name.data, form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Usuário registrado', 'success')
                return redirect(url_for('core.index'))
            except IntegrityError:
                db.session.rollback()
                flash('Erro! Email {} or user  {} já existe.' .format(form.name.data, form.email.data), 'error')
    return render_template('register.html', form=form)

