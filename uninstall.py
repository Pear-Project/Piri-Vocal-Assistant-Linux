#! /usr/bin/env python
import os
from os import system
from time import sleep

if os.geteuid() != 0:
    print("\033[31mError: \033[0mPlease run this script as superuser/sudo")
    exit()

system("sudo rm -rf /usr/lib/piri /usr/share/applications/piri /usr/bin/piri /usr/bin/pirivoice.py")
print("\033[35mAlert: \033[0mDone uninstalling items...")
sleep(0.5)
print("\033[35mAlert: \033[0mStarting post install verification")
sleep(2)
if not os.path.exists("/usr/lib/piri"):
    print("\033[34mSuccess: \033[0mpiri has been removed from /usr/lib")
else:
    print("\033[31mError: \033[0m/usr/lib/piri wasn't removed. Try again.")
if not os.path.exists("/usr/share/applications/piri"):
    print("\033[34mSuccess: \033[0mpiri has been removed from /usr/share/applications")
else:
    print("\033[31mError: \033[0m/usr/share/applications/piri wasn't removed. Try again.")
if not os.path.exists("/usr/bin/piri"):
    print("\033[34mSuccess: \033[0mpiri has been removed from /usr/bin")
    else:
    print("\033[31mError: \033[0m/usr/bin/piri wasn't removed. Try again.")
if not os.path.exists("/usr/bin/pirivoice.py"):
    print("\033[34mSuccess: \033[0mpirivoice.py has been removed from /usr/bin/pirivoice.py")
else:
    print("\033[31mError: \033[0m/usr/bin/pirivoice.py wasn't removed. Try again.") 