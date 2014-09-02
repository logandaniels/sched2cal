from icalendar import Calendar, Event

class Calendarizer:
    def __init__(self, courses):
        self.courses = courses
        cal = Calendar()
