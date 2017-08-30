"""
The following is a program for a fictional company that has just opened two new branches: 
one in New York City, the other in London. The program will print out whether the branches are open or
closed based on the current time of the headquarters here in Portland. The hours of both
branches are 9:00AM - 9:00PM in their own time zone. The program uses Python 2.7 and IDLE.
"""


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


