from project import db


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
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)                 # TEMPORARY - TO BE DELETED IN FAVOR OF HASHED PASSWORD

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return 'User: {}' .format(self.name)

