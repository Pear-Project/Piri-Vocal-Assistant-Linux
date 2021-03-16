#!/bin/python3

import speech_recognition as sr
import os
import re
import time
import sys
import subprocess


r = sr.Recognizer()
pid = os.fork()
if pid == 0:
    os.system("/usr/share/piri-assistant/passive.gambas")

listening = 0

def listen(listening, source):
    if listening == 0:
        os.system("playerctl pause") #pauses music so the assistant can be understood better
        listening = 1
        os.system("ffplay -nodisp -autoexit /usr/share/piri-assistant/piri-open.mp3 >/dev/null 2>&1")
        print("talk")
        audio_text=r.listen(source)
        print("done")
        if audio_text == "":
            print("nothing said")

        try:
            text = r.recognize_google(audio_text) #converts speech to text
            print(text)
            if text.__contains__("test"):
                activator, translation3, filler, targetLang=text.split(" ") #splits the command into each word for parsing  #no ideea what s this
            elif text.__contains__("in browser"):
                #strips the unnecesary parts of the command
                suche=text.replace("in browser", "")
                suche=suche.strip("open")
                suche=text.replace("open", "") # strips the unnecesary parts
                suche = suche.strip()
                suche = suhe.replace(" ", "-")
                print(suche.lower())
                suche_tts = suche.replace(" ", "+")
                #------------------------------------------
                os.system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+suche_tts+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1") # plays a conformation text
                os.system("xdg-open 'https://duckduckgo.com/?q="+suche+"'") # opens the requested thing in duckduckgo
            elif text.__contains__("Browser"):
                os.system("mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=opening+your+browser' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
                os.system("firefox &") # just opens firefox
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
            elif text.__contains__("browser"):
                os.system("mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=opening+your+browser' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1") # plays conformation message
                os.system("firefox &") # just starts firefox
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
            elif text.__contains__("calculator"):
                os.system("mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+calculator' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1") # conformation message
                os.system("kcalc &") # opens kcalc (calculator)
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
                os.system('kill %d' % os.getpid())
            elif text.__contains__("file manager"):
                os.system("mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+your+file+manager' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1") # conformation message
                os.system("nautilus &") # open nautilus
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
            elif text.__contains__("open"):
                program=text.replace("open", "") # strips the unnecesary parts
                program = program.strip()
                program = program.replace(" ", "-")
                print(program.lower())
                program_tts = program.replace(" ", "+")
                os.system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+program_tts+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1") # play confirmation message
                os.system("bash /usr/share/piri-assistant/programmopener.sh "+program.lower()) # launches the programmopener module and passes the porgramm to open
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
            elif text.__contains__("Wikipedia"):
                wiki = text.replace("search Wikipedia for", "") # strips unnecesary parts
                wiki = text.replace("search on Wikipedia for", "")
                wiki = wiki.strip()
                print(wiki.lower())
                wiki_tts = wiki.replace(" ", "+")
                os.system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+searching+"+wiki_tts+"+on+wikipedia' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
                os.system("xdg-open 'https://en.wikipedia.org/wiki/"+wiki+"'") # search for the term specified by the user via wikipedia
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
            else:
                os.system("sh /usr/share/piri-assistant/googlesearch -py '"+text+"'") # launches the googlesearch module and passes the term to search for further processing
                #listening = 0
                os.system("kill $(pgrep piri.py) && killall gbr3")
                sys.exit(0)
                pass
                os.system('kill %d' % os.getpid())
        except:
            print("error (listener)")
            listening  = 0
            os.system("sh /usr/share/piri-assistant/googlesearch -err") # if an error occured it launches the googlesearch module to say an error message
            os.system("ffplay -nodisp -autoexit /usr/share/piri-assistant/piri-close.mp3 >/dev/null 2>&1")
        os.system("playerctl play") #launches the previously stopped music again
        os.system("kill $(pgrep piri.py) && killall gbr3")
        sys.exit(0)
        pass
        os.system('kill %d' % os.getpid())

while listening != 1:
    with sr.Microphone() as source:
        listen(listening, source)        
