#Sched2Cal
A Python utility for automatically creating Google Calendar events for your University of Minnesota courses.

##Description
Each semester I find myself going through my U of M enrollment summary and manually adding each lecture, lab, and discussion section as a recurring event in my calendar. It's awesome for staying organized, but it's a pain. That's why I made sched2cal. It parses the course information on your registration summary page and translates your courses into calendar events with proper titles, recurrences, and locations. You can import the resulting iCalendar file directly into your Google Calendar.

##Prerequisites

The following libraries are required to make this happen:
- mechanize for x500 authentication and grabbing the enrollment summary
- BeautifulSoup for parsing the HTML
- icalendar for producing the .ics output

##Usage

From the command line, simply run
`python sched2cal.py`
    
You'll be asked to provide your x500 username and password so that the script can access your enrollment summary. It should then do its thing and create a file called "SpringCourses2015.ics" that you can directly import into your Google Calendar.


##Notes

This utility should still work even if you use a different calendar service (Yahoo, Mac's Calendar app, etc.), since .ics import is pretty widely supported.

##TODO

- Light GUI
- Support for event reminders