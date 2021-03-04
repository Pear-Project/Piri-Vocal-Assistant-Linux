#!/bin/python3

import speech_recognition as sr
import os
from gtts import gTTS
import time
import subprocess

r = sr.Recognizer()
os.system("rm $HOME/.local/vAssistant/listening.lock")
def translation(targetLang):
    targetLangS="en"
    targetLang=targetLang.lower()
    if   targetLang == "german":
        targetLangS="de"
    elif targetLang == "african":
        targetLangS="af"
    elif targetLang == "arabic":
        targetLangS="ar"
    elif targetLang == "bengali":
        targetLangS="bn"
    elif targetLang == "bosnian":
        targetLangS="bs"
    elif targetLang == "catalan":
        targetLangS="cs"
    elif targetLang == "welsh":
        targetLangS="cy"
    elif targetLang == "danish":
        targetLangS="da"
    elif targetLang == "greek":
        targetLangS="el"
    elif targetLang == "english":
        targetLangS="en"
    elif targetLang == "esperanto":
        targetLangS="eo"
    elif targetLang == "spanish":
        targetLangS="es"
    elif targetLang == "estonian":
        targetLangS="et"
    elif targetLang == "finnish":
        targetLangS="fi"
    elif targetLang == "french":
        targetLangS="fr"
    elif targetLang == "gujarati":
        targetLangS="gu"
    elif targetLang == "hindi":
        targetLangS="hi"
    elif targetLang == "croatian":
        targetLangS="hr"
    elif targetLang == "hungarian":
        targetLangS="hu"
    elif targetLang == "armenian":
        targetLangS="hy"
    elif targetLang == "indonesian":
        targetLangS="id"
    elif targetLang == "icelandic":
        targetLangS="is"
    elif targetLang == "italian":
        targetLangS="it"
    elif targetLang == "japanese":
        targetLangS="ja"
    elif targetLang == "javanese":
        targetLangS="jw"
    elif targetLang == "khmer":
        targetLangS="km"
    elif targetLang == "kannada":
        targetLangS="kn"
    elif targetLang == "korean":
        targetLangS="ko"
    elif targetLang == "latvian":
        targetLangS="lv"
    elif targetLang == "macedonian":
        targetLangS="mk"
    elif targetLang == "malayalam":
        targetLangS="ml"
    elif targetLang == "marathi":
        targetLangS="mr"
    elif targetLang == "myanmar":
        targetLangS="my"
    elif targetLang == "nepali":
        targetLangS="ne"
    elif targetLang == "dutch":
        targetLangS="nl"
    elif targetLang == "norwegian":
        targetLangS="no"
    elif targetLang == "polish":
        targetLangS="pl"
    elif targetLang == "portuguese":
        targetLangS="pt"
    elif targetLang == "romanian":
        targetLangS="ro"
    elif targetLang == "russian":
        targetLangS="ru"
    elif targetLang == "sinhala":
        targetLangS="si"
    elif targetLang == "slovak":
        targetLangS="sk"
    elif targetLang == "albanian":
        targetLangS="sq"
    elif targetLang == "serbian":
        targetLangS="sr"
    elif targetLang == "sundanese":
        targetLangS="su"
    elif targetLang == "swedish":
        targetLangS="sv"
    elif targetLang == "swahili":
        targetLangS="sw"
    elif targetLang == "tamil":
        targetLangS="ta"
    elif targetLang == "telugu":
        targetLangS="te"
    elif targetLang == "thai":
        targetLangS="th"
    elif targetLang == "filipino":
        targetLangS="tl"
    elif targetLang == "turkish":
        targetLangS="tr"
    elif targetLang == "ukraninan":
        targetLangS="uk"
    elif targetLang == "urdu":
        targetLangS="ur"
    elif targetLang == "vietnamese":
        targetLangS="vi"
    elif targetLang == "chinese":
        targetLangS="zh-CN"
    elif targetLang == "mandarin":
        targetLangS="zh"
    return(targetLangS)

def listen(source):
    if os.path.isfile(+"$HOME/.local/vAssistant/listening.lock") == "False":
        os.system("echo 'LISTENING' > $HOME/.local/vAssistant/listening.lock")
        playing=subprocess.check_output("playerctl status", shell=True) # check if media is playing, to not just show a random error/warning
        if playing.lower.__contains__("playing"):
            os.system("playerctl pause") #pauses music so the assistant can be understood better
            stoppedmusic=False
        os.system("paplay $HOME/.local/vAssistant/listening.wav")
        print("talk")
        audio_text=r.listen(source)
        print("done")
        if audio_text == "":
            print("nothing said, nothing done")

        try:
            text = r.recognize_google(audio_text) #converts speech to text
            print(text)
            if text.__contains__("translate"):
                # translation module
                activator, translation3, filler, targetLang=text.split(" ") #splits the command into each word for parsing
                if targetLang == "":
                    targetLang=filler #sets the filler to the target language if the targetlanguage is empty, when the user said something like "translate x english"
                targetLangS=translation(targetLang)
                print(translation3)
                ##change the called language to it's short form
                print(targetLangS) #prints the short form of the called language, used for development reasons
                os.system("sh $HOME/.local/vAssistant/translate '"+translation3+"' "+targetLangS+" "+targetLang) # calls the translation module and passes all the requierd data
            elif text.__contains__("in browser"):
                #strips the unnecesary parts of the command
                suche=text.replace("in browser", "")
                suche=suche.strip("open")
                #------------------------------------------
                os.system("gtts-cli 'ok, searching for "+suche+" in your browser' | mpg123 -") # plays a conformation text
                os.system("xdg-open 'https://duckduckgo.com/?q="+suche+"'") # opens the requested thing in duckduckgo
            elif text.__contains__("Browser"):
                os.system("gtts-cli 'ok, opening firefox' | mpg123 -") # plays conformaiton message
                os.system("firefox & disown") # just opens firefox
            elif text.__contains__("browser"):
                os.system("gtts-cli 'ok, opening firefox' | mpg123 -") #plays conformation message
                os.system("firefox & diswon") # just starts firefox
            elif text.__contains__("calculator"):
                os.system("gtts-cli 'ok, opening the Calculator' | mpg123 -") # conformation message
                os.system("kcalc & disown") # opens kcalc (calculator)
            elif text.__contains__("taschenrechner"):
                os.system("gtts-cli 'ok, opening the Calculator' | mpg123 -") #play conformation
                os.system("kcalc & disown") # opens kcalc (calculator)
            elif text.__contains__("file manager"):
                os.system("gtts-cli 'ok, opening your File manager' | mpg123 -") # conformation message
                os.system("dolphin & disown") # opens dolphin
                os.system("nautilus & disown") # open nautilus
            elif text.__contains__("stocks"):
                suche=text.replace("stocks", "") # strips unnencesary parts
                os.system("gtts-cli 'searching for "+suche+" stocks' | mpg123 -") # plays confirmation message
                os.system("xdg-open 'https://duckduckgo.com/?q="+suche+"+stocks&t=h_&ia=stock'") # open searched companies stocks via duckduckgo
            elif text.__contains__("open"):
                program=text.replace("open", "") # strips the unnecesary parts
                os.system("gtts-cli 'ok, opening "+program+"' | mpg123 -") # play confirmation message
                os.system("sh /home/ali/.local/vAssistant/programmopener.sh "+program) # launches the programmopener module and passes the porgramm to open
            elif text.__contains__("Wikipedia"):
                wiki=text.replace("search Wikipedia for", "") # strips unnecesary parts
                os.system("gtts-cli 'ok, searching for "+wiki+"on wikipedia' | mpg123 -") # play confirmation message
                os.system("xdg-open 'https://en.wikipedia.org/wiki/"+wiki+"'") # search for the term specified by the user via wikipedia
            else:
                os.system("sh $HOME/.local/vAssistant/googlesearch -py '"+text+"'") # launches the googlesearch module and passes the term to search for further processing

        except:
            print("error (listener)")
            os.system("sh $HOME/.local/vAssistant/googlesearch -err") # if an error occured it launches the googlesearch module to say an error message
        if stoppedmusic==True: #checks if media got stopped previously, to not start media paused by the user
            os.system("playerctl play") #launches the previously stopped music again
        os.system("rm $HOME/.local/vAssistant/listening.lock")

while not os.path.isfile("/home/ali/.local/vAssistant/listening.lock"):
    with sr.Microphone() as source:
            restart = 0
            activatorText=""
            print("talk (activator)")
            audio_text=r.listen(source) #listens for the activator
            print("done (activator)")


            print(audio_text)
            if audio_text is not None:
                try:
                    activatorText=r.recognize_google(audio_text) #converts speech to text
                    print(activatorText) #prints the text said by the user for development reasons
                    activatorText=activatorText.lower()
                    if activatorText.__contains__("hey assistant"): #checks if the activator was the set activator (the activator has to be lowercase!)
                        listen(source) #calls the command function and passes two necessary values
                    elif activatorText.__contains__("ok assistant"):
                        listen(source)
                    else:
                        print(activatorText) #prints the text said by the user for development reasons
                        print("activator not correct") #prints the error in the command line (only visible if ran from terminal)
                except:
                    print("error") #if an error with the speech recognition occurs it just prints "error" in the command line
