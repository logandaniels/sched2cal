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