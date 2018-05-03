from flask import render_template, Blueprint, request, redirect, url_for, flash
from project.models import Event
from .forms import *
from project import db


core_blueprint = Blueprint('core', __name__, template_folder='templates')


@core_blueprint.route('/')
def index():
    return render_template('index.html')


@core_blueprint.route('/eventos')
def list_events():
    all_events = Event.query.all()  # query events in the db
    return render_template('eventos.html', events=all_events)


@core_blueprint.route('/add_event', methods=['GET','POST'])
def add_event():
    form = AddEventForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            novo_evento = Event(form.event_prefix.data, form.event_xvm.data)
            db.session.add(novo_evento)
            db.session.commit()
            flash('Novo evento de {}, adicionado!' .format(novo_evento.prefix), 'success')
            return redirect(url_for('core.list_events'))
        else:
            flash_errors(form)
            flash('Erro! Evento não adicionado', 'error')
    return render_template('add_event.html', form=form)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'info')
