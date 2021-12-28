#! /usr/bin/python3

import speech_recognition as sr
import os
from os import system, sys
import socket
import platform 
import signal
from contextlib import contextmanager

if not os.path.exists("/usr/lib/piri"):
    print("\033[31mError: \033[34mpiri\033[0m doesn't exist in \033[35m/usr/lib\033[0m")
    exit()
try:
    import getdate
except:
    sys.path.insert(1, "/usr/lib/piri")
    import getdate


rec = sr.Recognizer()
#microphone = sr.Microphone(device_index=0)
verbose = False
standalone = False
if len(sys.argv) > 1:
    for x in range(len(sys.argv)):
        if sys.argv[x] == "-s" or sys.argv[x] == "--standalone":
            standalone = True
else:
    print("\033[35mWarning: \033[0mPiri has been launched in gui mode... Please add the suffix -s to launch it in CLI mode")
 
if platform.system() != "Linux":
    print(f"\033[31Error:\033[0m This application isn't meant to be ran on {platform.system()}")




@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, raise_timeout)
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)

    try:
        yield
    except TimeoutError:
        pass
    finally:
        # Unregister the signal so it won't be triggered
        # if the timeout is not reached.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)


def raise_timeout(signum, frame):
    raise TimeoutError

def wttmprd(s):
    system(f"rm -rf /tmp/read ; touch /tmp/read ; echo {s} >> /tmp/read")
def sendNotification(t):
    return f'notify-send -i /usr/lib/piri/piri_icon.png {t}'
    

def getInput():
    print("\033[34mInit\033[0m")
    if isInternet() is False:
        print("\033[31mError:\033[0m No internet is available")
        system(f'{sendNotification("internet is needed for piri to run")} ; ffplay -nodisp -autoexit failinter.mp3')
        exit()
   
        
    with sr.Microphone() as source:
        print("\033[34mAdjusting for ambient noise...\033[0m")
        rec.adjust_for_ambient_noise(source, duration=1)
        system("ffplay -nodisp -autoexit /usr/lib/piri/piri-open.mp3 ")
        wttmprd("User is speaking....")
        system(sendNotification('"Speak now"'))
        print("\033[31mSpeak:\033[0m")
        
        a = rec.listen(source)
        try:
            nr = rec.recognize_google(a)
        except:
            nr = ""
        return nr

def isInternet():
    try:
        with timeout(2): # better to use a timeout to kill the operation in the case of a recursive connection timeout or long response time
            socket.create_connection((("one.one.one.one"), 53))
        return True
    except OSError or Exception or TimeoutError:
        return False
    

def isFileindir(filename, directory):
	if not os.path.exists(directory) or not os.path.isdir(directory):
		return False
	for r,d,f in os.walk(str(directory)):
		for x in range(len(f)):
			if filename == f[x]:
				return True
			else:
				pass
	return False
def returnVoice(s):
    system(f"rm /tmp/piri/* ; mkdir -p /tmp/piri; curl -l 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text={s}' > /tmp/piri/reply.mp3 ; ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")

def isInt(s):
    try:
        x = int(s)
        return True
    except Exception:
        return False


####################################################################################################################################################################################################
        

def main():
        command = getInput()
        print(f"\033[35m{command}\033[0m")
        avail = False
        if command == "":
            print(f"\033[31mError:\033[0m couldn't get the command")
            system("rm -rf /tmp/read ; mkdir -p /tmp/read")
            wttmprd(f"\033[31mError:\033[0m couldn't get the command")
            system(sendNotification('"I couldn\'t quite get that, please try again."'))
            system("ffplay -nodisp -autoexit /usr/lib/piri/failunderstand.mp3")

        elif isInt(command): #deprecated for now
            print(f"\033[33m{command}\033[0m")

        elif command.__contains__("in browser"):
            cmd = command.replace("search", "", 1).replace("in browser", "").replace("open", "",1)

            if isInternet():
                c = cmd.replace(" ","+")
                returnVoice(f"opening {c} in browser".replace(" ", "+"))
                wttmprd(f"Opening {c} in browser")
                system(sendNotification(f'"Opening {c} in browser"'))
                system(f"nohup xdg-open https://www.google.com/search?q={cmd} &")

            else:
                print("\033[31mError:\033[0m No internet connection available")
                wttmprd("\033[31mError:\033[0m No internet connection available")
                system(sendNotification('"No internet connection available"'))
                system("ffplay nointernetavailable.mp3 -nodisp -autoexit")
                exit()
                
        elif command.__contains__("open"):
            cmd = command.split("open")
            comm = cmd[1].lstrip().rstrip().lower()
            print(f"\033[34m{comm}\033[0m")

            if isFileindir(comm, "/usr/bin"):
                if isInternet():
                    system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+cmd[1].replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
                wttmprd(f"Opening {cmd[1]}")
                system(sendNotification(f'"Opening {cmd[1]}"'))
                system(f"nohup {comm} &")
                avail = True
            
                        
            if not avail:
                print("\033[31mError:\033[0mFile not available in /usr/bin")
                system("mkdir -p /tmp/piri")
                if isInternet():
                    wttmprd(f"Opening {comm} in browser")     
                    system(sendNotification(f'"Opening {comm} in browser"'))
                    system(f"ffplay /usr/lib/piri/filenotavaillocal.mp3 -nodisp -autoexit ; xdg-open https://www.google.com/search?q={comm}")
                                  
                else:
                    system(sendNotification('"No internet connection"'))
                    system("ffplay /usr/lib/piri/nointernetavailable.mp3 -nodisp -autoexit")
                    wttmprd("No internet connection")
                    

        elif command.__contains__("date today"):
            date = getdate.getDate()
            wttmprd(f"it is {date}")
            system(sendNotification(f'"it is {date}"'))
            system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=the+date+today+is"+date.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
            print(f"\033[31m{date}\033[0m")
            
            
        
        elif command.__contains__("time now") or command.__contains__("time right now"):
            time = getdate.getTime()
            system(sendNotification(f'"it is {time}"'))
            wttmprd(f"it is {time}")
            system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=the+time+now+is"+time.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
            


        else:
            cl = command.lower()
            print("\033[31mError: \033[0mUnrecognized command, will try to parse using additional methods")
            if isFileindir(command.lower(), "/usr/bin"):
                wttmprd(f"Opening {command}")
                system(sendNotification(f'"Opening {command}"'))
                print("\033[35mFile available in /usr/bin\033[0m")
                if isInternet():
                    system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+command.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
                
                system(f"nohup {command.lower()} &")
                avail = True
            if not avail:
                print("\033[31mError:\033[0mFile not available in /usr/bin")
                system("mkdir -p /tmp/piri")
                wttmprd(f"Opening {command} in browser")
                system(sendNotification(f'""Opening {command} in browser"'))
                system(f"ffplay /usr/lib/piri/filenotavaillocal.mp3 -nodisp -autoexit ; nohup xdg-open https://www.google.com/search?q={command} &")
                

                







        system("ffplay -nodisp -autoexit /usr/lib/piri/piri-close.mp3")
        

if standalone is True:
    main()
quit()
