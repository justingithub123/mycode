#!/usr/bin/python3
"""Python Parse a Log File"""

loginfail = 0
loginsuccess = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:
#loop over the list of lines

    for line in keystone_file:
        # look for the fail pattern => - - - - -]
        if "- - - - -] Authorization failed" in line:
                loginfail += 1
        elif "-] Authorization failed" in line:
                loginsuccess += 1

print("The number of failed login attempts is:", loginfail)
print("The number of successful login attempts is:", loginsuccess)
