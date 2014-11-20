import mechanize
import getpass
import sys

REGISTER_URL = "https://onestop2.umn.edu/registration/initializeCurrentEnrollment.do?institution=UMNTC&resetInstitut"
# It's called "Register" on Onestop, but it also
# provides a concise enrollment summary.

user = ""
password = ""

br = mechanize.Browser()
br.set_handle_robots(False)

def login():
    response = br.open(REGISTER_URL)
    br.select_form(name="lform") # Select the login form
    br["j_username"] = user
    br["j_password"] = password
    response = br.submit()

    if "Incorrect ID/Password" in response.read():
       return False
    return True

def getEnrollmentSummary():
    response = br.open(REGISTER_URL)
    pageText = response.read()
    if "login" in pageText.lower():
        if not login():
            raise Exception("Error logging in.")

    for form in br.forms(): # Select the Continue form on the no-Javascript page
        br.form = form
    response = br.submit()  # and click to continue

    for form in br.forms(): # And again. There are two identical pages.
        br.form = form
    response = br.submit()
    pageText = response.read()
    if "current enrollment by term" not in pageText.lower():
        raise Exception("Error reaching registration page.")
    return pageText


def grab():
    global user, password
    user = raw_input("Enter your x500 username: ")
    password = getpass.getpass("Enter your x500 password: ")
    print "Testing login..."
    if not login():
        sys.exit("Incorrect login details!")
    else:
        print "Login OK!\n"
    return getEnrollmentSummary()
