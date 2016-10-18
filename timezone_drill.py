from datetime import datetime, time
from pytz import timezone

london_dt = datetime.now(timezone('Europe/London'))
london = london_dt.strftime("%H,%M")

ny_dt = datetime.now(timezone('US/Eastern'))
ny = ny_dt.strftime("%H,%M")

def isOpen(city):
    
    city = city.split(",")
    if time(int(city[0]), int(city[1]))  >= time(9, 0) and time(int(city[0]), int(city[1])) <= time(21, 0):
        print "The office is open."
    else:
        print "The office is closed."


