# Piri Backend + Frotend GUI

Piri is a voice assistant made for pearOS, with macOS design in mind. This project is now under re-development(backend) because of some Copyright issues (original Fork changed license in mid-developmet)
It was written in Python and Shell (bash)

## Features
- Easily modifiable source
- Simple way to add (custom) modules
- Some hardcoded features such as:
    - Google search
    - App opener
    - Good looking UI
    - Sound when it is waitng for commands
    - Sound when it fails


## Installation (from source):
I have created a rudimentary install file that can be ran by doing `python3 install-dependencies.py`, that just installs the dependencies for you in pip, but for your system dependencies, you'll have to do it through your package manager or any other way


**N/B:** I have personally experienced a lot of problems with installing PyAudio through pip, so if you also do, please install it through your package manager. Usually available as `python3-PyAudio` or `python3-pyaudio`


**Python** (should be available in all repositories as `python`)

**Pip** (in some package managers it is called `python3-pip` and in some it is called `python-pip`... Watchout though. python-pip can be for python2 and python3-pip for python3 so get the python3 version)

**pulseaudio** (should be available in all package managers as `pulseaudio`)

**gambas3** (very important in running the GUI version of piri, but unneeded in running the CLI (backend) version. Please install it if you plan to run the front-end)

**ffplay** (should be available in most package managers as `ffplay`)

**Pyaudio** `sudo pip3 install pyaudio`

**speech_recognition** `sudo pip3 install SpeechRecognition`

**Requests** `sudo pip3 install requests`

(OPTIONAL DEPENDENCIES)

**psmisc** (has been deprecated for now but I'd recommend installing it as the command `killall` might be used in later versions)



After all dependencies are installed, you can run `python3 install.py` to install piri onto your system, and after, Piri is accessible by the start menu

## Usage:

You can launch the assistant from terminal after installing: `piri` for GUI verion and `pirivoice .py --standalone` or `pirivoice.py -s` for CLI version


**IF YOU RUN THE COMMAND LINE VERSION**
- You will see some warnings/errors at first, which are normal, after that it will print out "talk"
- it will print what was recognized and if the activator is correct it will print "talk", you will also hear a sound and a notification will be displayed on screen
- say your commands, and Piri will _try_ to execute them.

**IF YOU RUN THE GUI VERSION**
- Click the piri icon, and after a few seconds, you'll here a beep and a notification telling you to speak
- It can take upto a few seconds to parse your command, but after, it will tell you wht it was able to find from the command and execute it

## Telemetry/Data collection:
Piri does not directly collect any personal data nor recordings from users, because we (devs) don't need to.

**NOTE: **Data can be collected by 3rd parties such as Google (Google Text to Speech API)

The assistant also uses Google's TTS URL API (http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=example+of+a+random+text+here+xd)
The text to speech is powered by Google


## Notes
I did not test the consistency of the app, I ran basic tests. Feel free to improve it. In case if something goes wrong, start an issue. Thanks :p

<!---

## Useless, do not read the installation from deb package

## Installation(from .deb package): 
- First install the requirements _(you can copy the script below, or run command by command)_
```sh
#!/bin/bash
sudo apt-get install python3-pip -y
sudo add-apt-repository ppa:gambas-team/gambas-daily -y
sudo apt update
sudo apt-get install gambas3 -y
pip3 install SpeechRecognition pydub
pip3 install gtts
pip3 install jq
pip3 install googletrans==3.1.0a0
sudo apt install python3-pyaudio -y
sudo apt install golang-go -y
sudo apt install playerctl -y
sudo apt install recode -y
```
 -->
