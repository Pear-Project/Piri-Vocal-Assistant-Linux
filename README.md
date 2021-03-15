# Piri (backend)

Piri is a voice assistant made for pearOS, with macOS design in mind. This project is forked on axtloss/vAssistant repo.
It was written in Python and Shell (bash)

## Features
- Easily modifiable source
- Simple way to add (custom) modules
- some hardcoded features such as:
    - a translator, which supports 60 languages(speech wise, all languages are supported but might not be pronounced right)
    - google search
    - app opener
    - search for stocks of a specifc company
    - and much more, which you can explore yourself

## Usage:

You can launch the assistant(vAssitant.py) from the terminal:
- You will see some warnings/errors at first, which are normal, after that it will print out "talk(activator)"
    - the activator is "hey Piri" or "ok Piri" on standart, but can be changed at line 217 and 220 of the pyhton script
- it will print what was recognized, and if the activator is correct it will print "talk", you will also hear a sound
- then it will listen to the actual command

Or, you put the vAssistant.py in your autostart and then log out, and back in. The assistant will be started on login after that.

## Telemetry/Data collection:
Piri does not directly collect any personal data nor recordings from users, because we(devs.) don't need to. Data can be collected by 3rd parties such as google.

The assistant also uses Google's TTS URL API (http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=example+of+a+random+text+here+xd)
