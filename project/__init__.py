# indicate to the Python interpreter that this directory is a Python package
# also, creates the instance of the Flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# config:

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


from project.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

# blueprints:
from project.users.views import user_blueprint
from project.core.views import core_blueprint

# register the blueprints:
app.register_blueprint(user_blueprint)
app.register_blueprint(core_blueprint)
