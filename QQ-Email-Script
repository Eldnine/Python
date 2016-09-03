import smtplib
from getpass import getpass

def prompt(prompt):
    return input(prompt).strip()

fromaddrs = prompt("From: ")
toaddrs = prompt("To: ").split() #split required or get bug
# ie. to address a@d.com & b@d.com instead of ab@d.com

subject = prompt("subject: ")
print("Enter message: ")

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
    %(fromaddrs, ", ".join(toaddrs), subject))

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP_SSL('smtp.qq.com')

server.set_debuglevel(1)

print("Please input account and password")
username = prompt("Username: ")
password = getpass("Password: ")
server.login(username, password)
server.sendmail(fromaddrs, toaddrs, msg)

server.quit()
