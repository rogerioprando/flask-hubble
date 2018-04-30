# indicate to the Python interpreter that this directory is a Python package
# also, creates the instance of the Flask module
from flask import Flask

# config:

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# blueprints:

from project.users.views import user_blueprint
from project.core.views import core_blueprint

# register the blueprints

app.register_blueprint(user_blueprint)
app.register_blueprint(core_blueprint)
