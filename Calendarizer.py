import gflags
import httplib2
import json
from datetime import date, time, datetime

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS
FLAGS.auth_local_webserver = False

# format: YYYYMMDD

CLASSES_START_DATE = "20140902"
CLASSES_END_DATE =  "20141210"
DAY_CONVERSIONS = { "M" : "MO", "T" : "TU", "W" : "WE", "TH" : "TH", "F" : "FR" }
ISO_DAY_NUMBERS = { "M" : 1, "T" : 2, "W" : 3, "Th" : 4, "F" : 5}

# Set up a Flow object to be used to authenticate.

FLOW = OAuth2WebServerFlow(
    client_id='446570179058-15657jldrum21k7vsj6rabsmf1la16da.apps.googleusercontent.com',
    client_secret='23w0I9E09YKSGBTMZiD_gZjY',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='SCHED2CAL/1.0')


class Calendarizer:
    def __init__(self, courses):
        self.courses = courses

        pass

        # If the Credentials don't exist or are invalid, run through the native client
        # flow. The Storage object will ensure that if successful the good
        # Credentials will get written back to a file.
        storage = Storage('calendar.dat')
        credentials = storage.get()
        if credentials is None or credentials.invalid == True:
            credentials = run(FLOW, storage)

        # Create an httplib2.Http object to handle our HTTP requests and authorize it
        # with our good Credentials.
        http = httplib2.Http()
        http = credentials.authorize(http)

        # Build a service object for interacting with the API. Visit
        # the Google Developers Console
        # to get a developerKey for your own application.
        self.service = build(serviceName='calendar', version='v3', http=http)


    def getEvents(self):
        events = []
        for course in self.courses:
            event = json.dumps({
                "summary" : course.getTitle(),
                "start" : {
                    "dateTime" : self.getFirstClassDate(course) + self.formatTime(course.getStartTime())
                },
                "end" : {
                    "dateTime" : self.getFirstClassDate(course) + self.formatTime(course.getEndTime())
                },
                "location" : course.getLocation(),
                "recurrence" : "RRULE:FREQ=DAILY;BYDAY=" + ",".join(self.getRecurrence(course)) + 
                    ";UNTIL=" + CLASSES_END_DATE,
            })
            events.append(event)
        return events

    def formatTime(self, rawTime):
        timeObject = datetime.strptime(rawTime, "%I:%M %p")
        return timeObject.strftime("%H:%M:00.000-06:00")

    def getRecurrence(self, course):
        recurrence = []
        days = course.getDays()
        # reverse sort so that we always remove Th before T
        for month in sorted(DAY_CONVERSIONS.keys(), reverse=True):
            if month in days:
                days.replace(month, "", 1)
                recurrence.append(DAY_CONVERSIONS[month])
        return recurrence


    def getFirstClassDate(self, course):
        days = course.getDays()
        datetimeObj = datetime.strptime(CLASSES_START_DATE, "%Y%m%d")
        while not self.dayMatch(days, datetimeObj.isoweekday()):
            print "" + str(datetimeObj.isoweekday()) + " is not any of " + days
            datetimeObj = datetimeObj.replace(day=(datetimeObj.day + 1))
        return datetime.strftime(datetimeObj, "%Y-%m-%dT")

    def dayMatch(self, days, isoNum):
        # this function checks if any of the days, passed as a string of
        # the form "MWF", match the given iso weekday number

        # reverse so we check Th first
        possibleDays = sorted(ISO_DAY_NUMBERS.keys(), reverse=True)
        for day in possibleDays:
            if day in days:
                if ISO_DAY_NUMBERS[day] == isoNum:
                    return True
                days.replace(day, "", 1)
        return False


    def Calendarize(self):
        pass
        events = self.getEvents()

