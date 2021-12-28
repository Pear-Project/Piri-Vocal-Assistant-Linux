#! /usr/bin/env python3

import os
from os import system
import sys
import socket
import getdate

#prefixgoogleapi = "http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=" ##Deprecated

if os.name == "nt":
	print("\033[31mError:\033[0m this program isn't meant to be run on Windows")
	exit()
else:
	pass

#pid = os.fork()

"""if pid == 0:
	if os.path.exists("/usr/share/piri-assistant"):
		system("/usr/share/piri-assistant/passive.gambas")
	elif not os.path.exists("/usr/share/piri-assistant"):
		print("piri-assistant doesn't exist in \033[31m/usr/share \033[0m")
		exit()"""
def isInternet():
	try:
		socket.create_connection((("1.1.1.1"), 53))
		return True
	except OSError:
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

		

def getInput():
	
	system("ffplay -nodisp -autoexit piri-open.mp3")
	avail = False
	print("\033[35mCommand:\033[0m")
	command = str(input())
	if command.__contains__("in browser"):
		cmd = command.replace("in browser", "").replace("open", "",1)
		if isInternet():
			c = cmd.replace(" ","+")
			system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+c+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
			system(f"xdg-open https://www.google.com/search?q={c}")
		else:
			print("\033[31mError:\033[0m No internet connection available")
			system("ffplay nointernetavailable.mp3 -nodisp -autoexit")
			exit()
			
	elif command.__contains__("open"):
		cmd = command.split("open")
		comm = cmd[1].lstrip().rstrip().lower()
		print(f"\033[34m{comm}\033[0m")
		if isFileindir(comm, "/usr/bin"):
			if isInternet():
				system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+cmd[1].replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
			system(comm)
			avail = True
		
					
		if not avail:
			print("\033[31mError:\033[0mFile not available in /usr/bin")
			if isInternet():
				system(f'ffplay filenotavaillocal.mp3 -nodisp -autoexit ; xdg-open https://www.google.com/search?q={comm.replace(" ", "+")}')
			else:
				system("ffplay nointernetavailable.mp3 -nodisp -autoexit")
	elif command.__contains__("date today"):
				date = getdate.getDate()
				system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=the+date+today+is"+date.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
				print(f"\033[31m{date}\033[0m")
			
	elif command.__contains__("time now"):
		time = getdate.getTime()
		system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=the+time+now+is"+time.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
			
	else:
		cl = command.lower()
		print("\033[31mError: \033[0mUnrecognized command, will try to parse using additional methods")
		if isFileindir(cl, "/usr/bin"):
			print("\033[35mFile available in /usr/bin\033[0m")
			system("rm /tmp/piri/*; mkdir -p /tmp/piri; curl 'http://www.google.com/speech-api/v1/synthesize?lang=en-us&text=okay+opening+"+cl.replace(" ", "+")+"' --output /tmp/piri/reply.mp3 && ffplay -nodisp -autoexit /tmp/piri/reply.mp3 >/dev/null 2>&1")
			system(cl)
			avail = True
		if not avail:
			print("\033[31mError:\033[0mFile not available in /usr/bin")
			system("mkdir -p /tmp/piri ; ")
			system("ffplay filenotavaillocal.mp3 -nodisp -autoexit")
			system(f"xdg-open https://www.google.com/search?q={command}")
	



	system("ffplay -nodisp -autoexit piri-close.mp3")
	


getInput()
exit()