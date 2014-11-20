from bs4 import BeautifulSoup
import bs4
import time
import Course

class CourseScraper:
    def __init__(self, htmlString):
        self.soup = BeautifulSoup(htmlString)

    def isClassRow(self, tag):
        return tag.name == "tr" and tag.has_attr("class") and not ("tableheader" in tag["class"])

    def getCourses(self):
        courses = []
        # first, let's find the table of course info
        table = self.soup.find(class_="coursetable")

        # each table row corresponds to a Course
        rows = table.find_all(self.isClassRow)

        for row in rows:
            prevRow = None

            # walk backwards until we find the previous tr tag
            for sibling in row.previous_siblings:
                if type(sibling) == bs4.element.Tag:
                    prevRow = sibling
                    break

            course = Course.Course()
            if row["class"] == prevRow["class"]:
                # same class means same course as previous, so pull the
                # course name from the previous row
                titleCell = prevRow.find(headers="t2")
            else:
                # find new course name
                titleCell = row.find(headers="t2")
            # now add the course title to the Course object with proper whitespace
            title = titleCell.find("a").string
            title = ' '.join(title.split())
            course.setTitle(title)

            # iterate through the table headers we care about,
            # parse a value out of each cell,
            # and add each value to the current Course

            sectionType = [string for string in row.find(headers="t3").stripped_strings][0]
            if "Lecture" in sectionType:
                sectionType = "LEC"
            elif "Lab" in sectionType:
                sectionType = "LAB"
            else:
                sectionType  = "DISC"

            course.setSectionType(sectionType)

            days = row.find(headers="t4").string.strip()
            course.setDays(days)

            times = [string for string in row.find(headers="t6").stripped_strings]
            startTime = times[0]
            endTime = times[2]
            course.setTimes(startTime, endTime)

            location = row.find(headers="t7").string
            course.setLocation(location)

            courses.append(course)
            if len(courses) == 0:
                raise Exception("Error parsing courses.")

        return courses