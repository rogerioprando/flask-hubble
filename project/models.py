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