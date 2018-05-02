import os

# grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control

SECRET_KEY = '<INSERT FROM RANDOM STRING GENERATED>'
DEBUG = True

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://rogerio:password@localhost/flask_hubble'
SQLALCHEMY_TRACK_MODIFICATIONS = True