from datetime import date, time, datetime
from icalendar import Calendar, Event
import pytz


# start/end date format: YYYYMMDD

CLASSES_START_DATE = "20150120"
CLASSES_START_DATETIME = datetime.strptime(CLASSES_START_DATE, "%Y%m%d")
CLASSES_END_DATE =  "20150508"
CLASSES_END_DATETIME = datetime.strptime(CLASSES_END_DATE, "%Y%m%d")

DAY_CONVERSIONS = { "M" : "MO", "T" : "TU", "W" : "WE", "Th" : "TH", "F" : "FR" }
ISO_DAY_NUMBERS = { "M" : 1, "T" : 2, "W" : 3, "Th" : 4, "F" : 5}

class iCalMaker:
    def __init__(self, courses):
        self.courses = courses
        print "\nPutting courses into a calendar file..."

    def getICS(self):
        '''Returns a string representation of an ics file containing
           an event for each course in the list of courses
           that was passed to the object's constructor.'''
        cal = Calendar()
        cal.add('prodid', '-//Sched2Cal UMN//umn.edu//')
        cal.add('version', '2.0')

        for course in self.courses:
            event = Event()
            start, end = self.getStartAndEnd(course)
            event.add("summary", course.getTitle())
            event.add("dtstart", start)
            event.add("dtend", end)
                #"timeZone" : "America/Chicago"
            event.add("location", course.getLocation())
            event.add("description", course.getLocation())
            event.add("rrule", {"FREQ" : ["DAILY"], "BYDAY" : self.getRecurrence(course),
                      "UNTIL" : CLASSES_END_DATETIME})
            cal.add_component(event)

        try:
            return cal.to_ical()
        except Exception, e:
            raise Exception("Error processing events.")

    def getStartAndEnd(self, course):
        startTime = datetime.strptime(course.getStartTime(), "%I:%M %p") # contains start time
        endTime = datetime.strptime(course.getEndTime(), "%I:%M %p") # contains end time

        dateObject = self.getFirstClassDate(course) # contains day

        # merge them to get datetime objects with correct date AND time
        start = startTime.replace(month=(dateObject.month), day=(dateObject.day),
                         year=(dateObject.year), tzinfo=pytz.timezone("US/Central"))
        end = endTime.replace(month=(dateObject.month), day=(dateObject.day),
                         year=(dateObject.year), tzinfo=pytz.timezone("US/Central"))
        return start, end

    def getRecurrence(self, course):
        '''returns a list of days to recur, according to the iCal standard'''
        recurrence = []
        courseDays = course.getDays()
        # reverse sort so that we always remove Th before T
        for day in sorted(DAY_CONVERSIONS.keys(), reverse=True):
            if day in courseDays:
                courseDays = courseDays.replace(day, "", 1)
                recurrence.append(DAY_CONVERSIONS[day])
        return recurrence


    def getFirstClassDate(self, course):
        '''returns a string representing the first day a class meets'''
        days = course.getDays()
        datetimeObj = CLASSES_START_DATETIME
        # step forward one day at a time until it's a day that the class meets 
        while not self.dayMatch(days, datetimeObj.isoweekday()):
            datetimeObj = datetimeObj.replace(day=(datetimeObj.day + 1))
        return datetimeObj

    def dayMatch(self, days, isoNum):
        '''returns True if any of the days, passed as a string of
        the form "MWF", match the given iso weekday number'''

        # reverse so we check Th first
        possibleDays = sorted(ISO_DAY_NUMBERS.keys(), reverse=True)
        for day in possibleDays:
            if day in days:
                if ISO_DAY_NUMBERS[day] == isoNum:
                    return True
                days = days.replace(day, "", 1)
        return False
