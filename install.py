#! /usr/bin/python3

import os
from os import sys, system
from time import sleep
import platform
print("########################## \033[34mWelcome to piri pre-alpha installer!\033[0m ##############################\n")
sleep(0.5)
if platform.system() != "Linux":
    print("\033[31mError: \033[0mThis script is meant to be ran on Linux")
    exit()
if not os.geteuid() == 0:
    print("\033[31mError: \033[0mPlease run the install script as superuser/sudo to give it necessary privileges")
    exit()
if os.path.exists("/usr/lib/piri"):
    print("\033[31mError: \033[0mPath \033[35m/usr/lib/piri\033[0m already exists. Do you want to overwrite it?")
    yn = str(input("\033[34m[y/n]: \033[0m"))
    if yn.__contains__("y"):
        print("\033[35mWarning: \033[0mOverwriting /usr/lib/piri")
        system("sudo rm -rf /usr/lib/piri")
    elif yn.__contains__("n"):
        print("\033[31Aborting: \033[0mUser has cancelled overwrite operation")
        exit()
    else:
        print("\033[31mError: \033[0mQuitting due to unexpected input")
        exit()
os.mkdir("/usr/lib/piri")
print("\033[35mWarning: \033[0mCreated the directory \033[34m/usr/lib/piri\033[0m")
system("sudo cp -r * /usr/lib/piri")


print("\033[35mAlert: \033[0mdo you want to create a shortcut at /usr/bin?")
yn = str(input("\033[34m[y/n]: \033[0m"))
if yn.__contains__("y"):
    print("\033[35mAlert: \033[0mCreating a shortcut at /usr/bin/")
    system("sudo cp -r pirivoice.py /usr/bin/ ; sudo chmod 755 /usr/bin/pirivoice.py")
    system("sudo cp -r bin/piri /usr/bin/ ; sudo chmod 755 /usr/bin/piri")
elif yn.__contains__("n"):
    print("\033[31mAborting: \033[0mNot creating a shortcut at /usr/bin")


print("\033[35mAlert: \033[0mdo you want to create a start menu (/usr/share/applications) shortcut?")
yn = str(input("\033[34m[y/n]: \033[0m"))
if yn.__contains__("y"):
    print("\033[35mAlert: \033[0mCreating a shortcut at /usr/share/applicatons")
    system("sudo cp -r bin/piri.desktop /usr/share/applications/")
elif yn.__contains__("n"):
    print("\033[31mAborting: \033[0mNot creating a shortcut at /usr/share/applications")

print("\033[35mAlert: \033[0mPost-install verification will be implemented soon :)")
sleep(2.5)



