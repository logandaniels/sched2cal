#Sched2Cal
A Python utility for automatically creating events for your University of Minnesota courses on your Google Calendar.

##Description
Each semester I find myself going through my U of M enrollment summary and manually adding each lecture, lab, and discussion section as a recurring event in my calendar. It's awesome for staying organized, but it's a pain. That's why I made sched2cal. It parses the course information on your registration summary page and authenticates with Google to add the events to your calendar, along with proper titles, recurrences, and locations.

##Prerequisites

The following libraries are required to make this happen:
- requests and httplib2 for grabbing pages
- BeautifulSoup for parsing the HTML
- gflags, apiclient, and oauth2client for authenticating with Google

##Usage

Navigate to your registration summary by clicking [here](https://webapps-prd.oit.umn.edu/registration/initializeCurrentEnrollment.do?institution=UMNTC) or by slicking _register_ on the onestop sidebar. When the page loads, save it into the sched2cal directory as `whatever-you-want.html`. At least on my Mac, I had to specify that Chrome save it as 'HTML only', rather than as 'Webpage Complete'.

Then, from the command line, simply run
`python sched2cal.py <html-filename>`
    
Your browser should pop up asking to authenticate with your Google account. Once you do so, the script should do its thing and create the events in your Google Calendar in a new subcalendar called *Fall 2014*. 

##Notes

It's ~~pretty~~ very rough in its current state, but it works. I'd like to make it download the HTML automatically, but the U doesn't seem to have a robust (public) API and I don't yet know how to mess with their authentication process. Also, currently a few settings are hardcoded for the Fall 2014 semester. In the future that should be calculated by the script.
