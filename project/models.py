from project import db
from sqlalchemy.ext.hybrid import hybrid_method



class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.Integer, nullable=False)
    xvm = db.Column(db.String, nullable=False)

    def __init__(self, prefix, xvm):
        self.prefix = prefix
        self.xvm = xvm

    def __repr__(self):
        return 'XVM: {}' .format(self.xvm)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)                 # TEMPORARY - TO BE DELETED IN FAVOR OF HASHED PASSWORD
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.authenticated = False

    @hybrid_method
    def is_correct_password(self, password):
        return self.password == password

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported"""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements"""
        return str(self.id)

    def __repr__(self):
        return '<User {0}>'.format(self.name)

