import os
from os import system, sys
import platform
from time import sleep
if platform.system() != "Linux":
    print("\033[31m This script is meant to be ran on Linux\033[0m")
    exit()
if os.geteuid() == 0:
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root -")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root \\")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root -")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root /") 
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root -")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root \\")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root -")
    sleep(0.5)
    system("clear")
    print("\033[35mWarning!: \033[0mThis script has been ran as root. It isn't recommended to run pip as root /") 
else:
    print("\033[35m!: \033[0m This script has not been ran as root")
if not os.path.exists("/usr/bin/python3"):
    print("\033[31mError: \033[0mPlease install python3")
    exit()
else:
    print("\033[34mSuccess:\033[0m python3 exists in /usr/bin")

if not os.path.exists("/usr/bin/pip3"):
    print("\033[31mError: \033[0mPlease install pip")
    exit()

else:
    print("\033[34mSuccess: \033[0m pip3 exists in /usr/bin")
if not os.path.exists("/usr/bin/ffplay"):
    print("\033[31mError: \033[0mPlease install ffplay")
    exit()
else:
    print("\033[34mSuccess: \033[0mffplay exists in /usr/bin")

if not os.path.exists("/usr/bin/gambas3"):
	print("\033[35mWarning: \033[31mTo use the gui version of piri, please install gambas3\033[0m\n")
else:
	print("\033[34mSuccess: \033[0m gambas3 exists in /usr/bin")

if not os.path.exists("/usr/bin/killall"):
	print("\033[35mWarning: \033[31mPiri will be semi-broken if the command killall is unavailable. Please install the package \033[34mpsmisc\033[0m\n")
else:
	print("\033[34mSuccess: \033[0m killall (psmisc) exists in /usr/bin")

#system("clear")
print("Attempting to fetch the following dependencies: \033[33mSpeechRecognition requests pyaudio\033[0m. In case of failure")
system("/usr/bin/pip3 install SpeechRecognition requests pyaudio")

#system("clear")
print("\033[34mRunning post-install validation check...\033[0m")
a = lambda : print("\033[35mSpeechRecognition\033[0m has been installed") if os.popen("pip list | grep SpeechRecognition").read().lower().__contains__("speechrecognition") else print("\033[31mError: \033[0mFailed to install SpeechRecognition. Please try again or install it through your package manager if possible")

b = lambda :print("\033[35mrequests\033[0m has been installed") if os.popen("pip list | grep requests").read().lower().__contains__("requests") else print("\033[31mError: \033[0mFailed to install requests. Please try again or install it through your package manager if possible")

c = lambda :print("\033[35mpyaudio\033[0m has been installed") if os.popen("pip list | grep PyAudio").read().lower().__contains__("pyaudio") else print("\033[31mError: \033[0mFailed to install pyaudio. Please try again or install it through your package manager if possible")

print(f"{a()}\n{b()}\n{c()}")
