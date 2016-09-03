#a script to check Singapore EP status
#requiremetns: instal splinter and chromedriver

from splinter import Browser
import smtplib

#email info
fromaddr = "From: xx@xx.com"
toaddrs = "To: xx@xx.com"
toaddrs = toaddrs.split()
server = smtplib.SMTP_SSL('smtp.xx.com')
username = "xx@xx.com"
password = ""

#personal info for input
FIN = ''
NAME = ''
PASSPORT = ''

def epstatus():
    with Browser('chrome') as browser:
        # Visit URL
        url = "https://eponline.mom.gov.sg/epol/PEPOLENQM007DisplayAction.do"
        browser.visit(url)

        if not browser.is_text_present('Application/Pass Status'):
            print "Unavailable now."
            return

        browser.fill('requesterNRICFIN', FIN)
        browser.fill('requesterName', NAME)
        button = browser.find_by_name('save')
        button.click()

        if not browser.is_text_present('Travel Document'):
            print "Unavailable/error."
            return

        browser.fill('travelDocNo', PASSPORT)
        button = browser.find_by_name('submitForm')
        button.click()

        if browser.is_text_present(': Pending'):
            print "Pending"
        else:
            print "Status changed!"
            sendEmail()

def sendEmail():
    def prompt(prompt):
        return input(prompt).strip()
    subject = "Status changed!"

    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
    %(fromaddr, ", ".join(toaddrs), subject))+("Status changed!")

    server.set_debuglevel(1)  # debug
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

epstatus()
