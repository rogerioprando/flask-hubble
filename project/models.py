from project import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property



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
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.Binary(60), nullable=False)
    password = db.Column(db.String, nullable=False)                 # TEMPORARY - TO BE DELETED IN FAVOR OF HASHED PASSWORD
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, password_text):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password_text
        self.authenticated = False

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password_text):
        self._password = bcrypt.generate_password_hash(password_text)

    @hybrid_method
    def is_correct_password(self, password_text):
        return bcrypt.check_password_hash(self._password, password_text)

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

