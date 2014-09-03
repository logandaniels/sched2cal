# This script was created by Logan Daniels.
# By using this script you assume full responsibility
# for any consequences or damages resulting from its use.
#
# USAGE: "python sched2cal.py <html filename>"
#
# Upon first running this script, a browser window will
# prompt you to grant the application access to your calendars.


import CourseScraper
import Calendarizer
import Course
import sys

def run():
    CS = CourseScraper.CourseScraper(sys.argv[1])
    myList = CS.getCourses()
    for course in myList:
        print(course)
    calMaker = Calendarizer.Calendarizer(myList)
    calMaker.calendarize()


if __name__ == "__main__":
    run()