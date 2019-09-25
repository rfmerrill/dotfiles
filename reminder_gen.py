#!/usr/bin/env python3

from ics import Calendar, Event
from datetime import datetime, timedelta, timezone
import pytz

NUM_MONTHS = 12
TIME = 18

cal = Calendar()
today = datetime.today()

pacific = pytz.timezone('US/Pacific')


def dayOfNthMonth(n, day):
    today = datetime.today()
    year = today.year
    month = (today.month + n) % 12 + 1
    year += int((today.month + n) / 12)
    return datetime(year, month, day, TIME)


for month in range(NUM_MONTHS):
    for day in (5, 20):
        the_date = dayOfNthMonth(month, day)
        if the_date.weekday() == 6:
            the_date -= timedelta(days=2)
        elif the_date.weekday() == 5:
            the_date -= timedelta(days=1)
        e = Event(name="Submit expense report")
        e.begin = pacific.localize(the_date).astimezone(timezone.utc)
        e.duration = timedelta(minutes=15)
        cal.events.add(e)

open("expense_reports.ics", "w").writelines(cal)
