# indicate to the Python interpreter that this directory is a Python package
# also, creates the instance of the Flask module
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
# import after instance,
from . import views
