from app.extensions import db
from app.models import Event
from datetime import date
from dateutil import easter

def populate_calendar():
    """ I will populate the calendar to fill up a possible empty page
        also it is a bit fun. Here's what in adding:
         · Bank holidays
         · Holidays
         · Season stulsis
    """
    
    
    for year in range(2023, 2060):
        # this will continue until 2060!
        ths_year_events = [
            Event(date=date(year, 12, 25),  event_title="Christmas day"),
            Event(date=date(year, 12, 26),  event_title="Boxing day"),
            Event(date=date(year, 1, 1),    event_title="New years day"),
            Event(date=easter.easter(year), event_title="Easter Sunday")
        ]
        for event in ths_year_events:
            db.session.add(event)
    db.session.commit()