# store the initial routes for web application

from . import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')
    #return "Hello World"
    # hello world may substituted by a html/css files
