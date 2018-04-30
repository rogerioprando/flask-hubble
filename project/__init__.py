# indicate to the Python interpreter that this directory is a Python package
# also, creates the instance of the Flask module
from flask import Flask

app = Flask(__name__)
# import after instance,
from . import views
