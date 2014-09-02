import CourseScraper
import Calendarizer
import Course

def test():
    CS = CourseScraper.CourseScraper("testhtml.html")
    myList = CS.getCourses()
    for course in myList:
        print(course)
    calMaker = Calendarizer.Calendarizer(myList)


if __name__ == "__main__":
    test()