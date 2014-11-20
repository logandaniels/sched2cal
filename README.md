#Sched2Cal
A Python utility for automatically creating events for your University of Minnesota courses on your Google Calendar.

##Description
Each semester I find myself going through my U of M enrollment summary and manually adding each lecture, lab, and discussion section as a recurring event in my calendar. It's awesome for staying organized, but it's a pain. That's why I made sched2cal. It parses the course information on your registration summary page and authenticates with Google to add the events to your calendar, along with proper titles, recurrences, and locations.

##Prerequisites

The following libraries are required to make this happen:
- mechanize for x500 authentication and grabbing the enrollment summary
- BeautifulSoup for parsing the HTML
- httplib2, gflags, apiclient, and oauth2client for authenticating with Google

##Usage

From the command line, simply run
`python sched2cal.py`
    
You'll be asked to provide your x500 username and password. These stay local, so don't worry about me stealing your identity. Then your browser should pop up asking to authenticate with your Google account. Once you do so, the script should do its thing and create the events in your Google Calendar in a new subcalendar called *Spring 2015 Courses*. 

##Notes
To use this, you'll have to generate a client ID and client secret [as described here](https://developers.google.com/google-apps/calendar/auth) and place them in the appropriate locations in the FLOW object in Calendarizer.py.
