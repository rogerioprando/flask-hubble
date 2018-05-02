# temporary file

from project import db
from project.models import Event

# create the database and the database table
db.create_all()

# insert event data
event1 = Event(4135, '>RAX12,00626,020518145447-2747193-04847135070046,86405;ID=4135;#50A7;*36<')
event2 = Event(4135, '>RUS00,020518151413-2746676-04846523059238,86411;ID=4135;#50D8;*30<')
event3 = Event(3975, '>RUS00,020518150431-2760026-04855014017135,35711;ID=3975;#13CD;*4D<')
db.session.add(event1)
db.session.add(event2)
db.session.add(event3)

# commit the changes
db.session.commit()