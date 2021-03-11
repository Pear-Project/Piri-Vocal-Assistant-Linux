# vAssistant

vAssistant is a virtual assistant written in python, 
which supports modules in virtually any programming language.

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

## Installation instructions:
_the assistant has only been tested on Arch linux and Ubuntu, Windows and MacOS support might be limited_

## For Arch Linux:
you will first have to install the dependencies:
```sh
    pip3 install SpeechRecognition pydub
    pip3 install gtts
    pip3 install jq
    pip3 install recode
    pip install googletrans==3.1.0a0
    sudo pacman -S python3-pyaudio
    sudo pacman -S python3-gtts
    sudo pacman -S python3-recode
    sudo pacman -S golang-go
    sudo pacman -S playerctl
```

after that, you clone the github and run the installer script
```sh
    git clone https://github.com/axtloss/vAssistant.git
    cd vAssistant
    sh installer.sh
```

## For Ubuntu/Debian (based distros)
Install the dependcies:
```sh
    pip3 install SpeechRecognition pydub
    pip3 install gtts
    pip3 install jq
    pip3 install recode
    pip install googletrans==3.1.0a0
    sudo apt install python3-pyaudio -y
    sudo apt install python3-gtts -y
    sudo apt install python3-recode -y
    sudo apt install golang-go -y
    sudo apt install playerctl -y
```
after that, you clone the github and run the installer script
```sh
    git clone https://github.com/axtloss/vAssistant.git
    cd vAssitant
    sh installer.sh
```

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

## Development info:
The Modules are(on Linux) in ~/.local/share/vAssistant/

The Sounds (also on Linux) are in ~/.local/share/vAssistant/sounds/

When developing your own Modules, make sure that you're not obstructing the recognizier for other modules
## Notes:
the text to speech is a bit slow on ubuntu, this will probably be fixed in the next merge
some dependencies might be called different depending on what repositories you use, so if the assistant isn't working correctly, just check if everything is installed properly

I will happily accept any tests/installation guides for other Linux distributions/Windows/MacOS
