"""
Title: Datetime – Python 2.7 – IDLE
Scenario: The company you work for just opened two new branches. One is in New York City,
the other in London. They need a very simple program to find out if the branches are open or
closed based on the current time of the Headquarters here in Portland. The hours of both
branches are 9:00AM - 9:00PM in their own time zone.
What is asked of you:
Create code that will use the current time of the Portland HQ to find out the time in the NYC &
London branches, then compare that time with the branches hours to see if they are open or
closed.
Print out if each of the two branches are open or closed.
Guidelines:
● Use Python 2.7 IDLE
● Use Datetime Module
● Execute program on the Shell
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


