# This script was created by Logan Daniels.
# By using this script you assume full responsibility
# for any consequences or damages resulting from its use.
#
# Upon first running this script, a browser window will
# prompt you to grant the application access to your calendars.

import WebGrabber
import CourseScraper
import iCalMaker
import Course
import sys

def run():
    enrollmentSummaryHTML = WebGrabber.grab()
    CS = CourseScraper.CourseScraper(enrollmentSummaryHTML)
    courseList = CS.getCourses()
    print "The following courses were found:"
    for course in courseList:
        print(course)

    calMaker = iCalMaker.iCalMaker(courseList)
    ics = calMaker.getICS()

    # write the .ics file to the disk
    f = open("Spring2015Courses.ics", "w")
    f.write(ics)
    f.close()

    print ("""\nCalendarization successful! A file called "Spring2015Courses.ics" """ +
          """has been created for you to import into your Google Calendar.""")


if __name__ == "__main__":
    run()
