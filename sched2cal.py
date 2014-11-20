# This script was created by Logan Daniels.
# By using this script you assume full responsibility
# for any consequences or damages resulting from its use.
#
# Upon first running this script, a browser window will
# prompt you to grant the application access to your calendars.

import WebGrabber
import CourseScraper
import Calendarizer
import Course
import sys

def run():
    htmlString = WebGrabber.grab()
    CS = CourseScraper.CourseScraper(htmlString)
    myList = CS.getCourses()
    print "The following courses were found:"
    for course in myList:
        print(course)
    calMaker = Calendarizer.Calendarizer(myList)
    calMaker.calendarize()
    print """Calendarization successful! Check your Google Calendar for
    a new calendar called 'Spring 2015 Classes'."""


if __name__ == "__main__":
    run()