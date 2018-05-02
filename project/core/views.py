from flask import render_template, Blueprint
from project.models import Event

core_blueprint = Blueprint('core', __name__, template_folder='templates')


@core_blueprint.route('/')
def index():
    return render_template('index.html')


@core_blueprint.route('/eventos')
def list_events():
    all_events = Event.query.all()  # query events in the db
    return render_template('eventos.html', events=all_events)
