#!/bin/bash

go get github.com/ericchiang/pup
cp $HOME/go/bin/pup $HOME/.local/bin/

curl -sL "https://raw.githubusercontent.com/Bugswriter/tuxi/main/tuxi" -o $HOME/.local/bin/tuxi
chmod +x $HOME/.local/bin/tuxi

mkdir $HOME/.local/vAssistant
cp googlesearch $HOME/.local/vAssistant/
mkdir $HOME/.local/vAssistant/sounds/
cp gc_message1.wav $HOME/.local/vAssistant/sounds/listening.wav
cp programmopener.sh $HOME/.local/vAssistant/
cp translate $HOME/.local/vAssistant/

chmod +x vAssistant.py
