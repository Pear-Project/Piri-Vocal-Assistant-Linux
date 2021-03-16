# Piri Backend + Frotend GUI

Piri is a voice assistant made for pearOS, with macOS design in mind. This project is forked on axtloss/vAssistant repo.
It was written in Python and Shell (bash)

## Features
- Easily modifiable source
- Simple way to add (custom) modules
- some hardcoded features such as:
    - google search
    - app opener
    - good looking UI
    - sound when it is waitng for commands
    - sound when it fails

## Installation:
- I added a failsafe, so you cannot run it as root :)
- git clone the project
- cd into it
- `./install.sh` _if it shows Permission Denied error, you have to `chmod +x install.sh` and re-run `./install.sh`_
- launch it from the application launcer(i.e. launchpad, application menu, app list etc.)

## Usage:

You can launch the assistant from terminal: `cd /path/to/piri.py && ./piri.py`
- You will see some warnings/errors at first, which are normal, after that it will print out "talk"
    - it does not need an activator when launched from terminal. Execute it and you are good to go
    - if you want to test it WITH the activator, `cd /path/to/piri.py && ./piri-activator`
      - say `hey Piri` _if it has been run from piri-activator_
- it will print what was recognized, and if the activator is correct it will print "talk", you will also hear a sound
- say your commands, and Piri will _try_ to execute them.

Or, you put the vAssistant.py in your autostart and then log out, and back in. The assistant will be started on login after that.

## Telemetry/Data collection:
Piri does not directly collect any personal data nor recordings from users, because we(devs.) don't need to. Data can be collected by 3rd parties such as google(Google Text to Speech)

The assistant also uses Google's TTS URL API (http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=example+of+a+random+text+here+xd)
The text to speech is powered by Google


## Notes
I did not tested the consistency of the app, I ran basic tests. Feel free to improove it. In case if something goes wrong, start an issue. Thanks :p

