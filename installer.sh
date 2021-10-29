#!/bin/bash

if [ "$(id -u)" == "0" ]; then
   echo "This is not meant to be ran as root :/" 1>&2
   exit 1
fi
    sudo apt-get install python3-pip -y
	pip3 install SpeechRecognition pydub
    pip3 install gtts
    pip3 install jq
    pip3 install googletrans==3.1.0a0
    sudo apt install python3-pyaudio -y
    sudo apt install golang-go -y
    sudo apt install playerctl -y
    sudo apt install recode -y

#creating folders part :)
mkdir -p /tmp/piri
sudo mkdir -p /usr/share/piri-assistant

#installing piri itself, with the TUXI module
sudo cp -r * /usr/share/piri-assistant
sudo mv /usr/share/piri-assistant/tuxi /usr/bin/tuxi
sudo mv /usr/share/piri-assistant/piri /usr/bin/
sudo mv /usr/share/piri-assistant/*.desktop /usr/share/applications
sudo mv /usr/share/piri-assistant/*.png /usr/share/icons/

#installing PUP module
go get github.com/ericchiang/pup
cp $HOME/go/bin/pup $HOME/.local/bin/

#installing jq and ffmpeg
sudo apt-get install jq -y
sudo apt-get install ffmpeg -y

