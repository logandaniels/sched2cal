from icalendar import Calendar, Event

CLASSES_START_DATE = "20140902"
CLASSES_END_DATE =  "20150508"

class Calendarizer:
    def __init__(self, courses):
        self.courses = courses
        cal = Calendar()

    def getEvents():
        for course in self.courses:
            event = Event()
            event.name = course.getTitle()
            event.begin

