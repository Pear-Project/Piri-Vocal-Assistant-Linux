# Piri (backend)

Piri is a voice assistant made for pearOS, with macOS design in mind. This project is forked on axtloss/vAssistant repo.
It was written in Python and Shell (bash)

For developing your own Modules, you only need:
- a programming language which can be called via python or the shell
- some basic python knowledge to be able to call the module(the source should make a good example)


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
    - the activator is "hey Assistant" or "ok Assistant" on standart, but can be changed at line 217 and 220 of the pyhton script
- it will print what was recognized, and if the activator is correct it will print "talk", you will also hear a sound
- then it will listen to the actual command

Or, you put the vAssistant.py in your autostart and then log out, and back in. The assistant will be started on login after that.

## Telemetry/Data collection:
The assitant uses for it's google search [tuxi](https://github.com/Bugswriter/tuxi) for the online search, which uses Google, if you know any alternatives to tuxi, that use duckduckgo or something similiar, i'd greatly accept it!
the Stock and in-browser search however use duckduckgo as it's search engine

The assistant also uses google's tts, speech recognition and translator, as they proved to work the best
