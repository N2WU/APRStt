#!/usr/bin/python
#
#
# Text-to-speech using Direwolf APRS Touchtone variables
# Coincides with custom APRS Direwolf config file
#
# Nolan Pearce, N2WU
#https://pythonbasics.org/text-to-speech/

import os
"""
import subprocess
import socket
import os

def execute_unix(inputcommand):
	p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	return output

"""
#we only need to edit and adjust "a"

obj_name = os.getenv('TTCALL')
status = os.getenv('TTSTATUS')
lat = os.getenv('TTLAT')
lon = os.getenv('TTLON')

#now do a very long 'if' statement to convert LAT back to milemarker. Assuming no points share LAT with different LON

if str(lat) = "41.354574":
	milemarker = "BIKE 0"
else if str(lat) = "41.344790":
	milemarker = "BIKE 1"
else if str(lat) = "41.338618 ":
	milemarker = "BIKE 2"
else if str(lat) = "41.327663":
	milemarker = "BIKE 3"
else if str(lat) = "41.330708":
	milemarker = "BIKE 4"
else if str(lat) = "41.322645":
	milemarker = "BIKE BRIDGE"
else if str(lat) = "41.342440":
	milemarker = "BIKE 5"
else if str(lat) = "41.343837":
	milemarker = "BIKE 6"
else if str(lat) = "41.359446":
	milemarker = "BIKE 7"
else if str(lat) = "41.371021":
	milemarker = "BIKE 8"
else if str(lat) = "41.376499":
	milemarker = "BIKE 9"
else if str(lat) = "41.386270":
	milemarker = "BIKE TEN OVERPASS"
else if str(lat) = "41.377957":
	milemarker = "BIKE ELEVEN"
else if str(lat) = "41.377957":
	milemarker = "BIKE TWELVE"
else if str(lat) = "41.359446":
	milemarker = "BIKE THIRTEEN"
else if str(lat) = "41.35457":
	milemarker = "RUN 0"
else if str(lat) = "41.348595":
	milemarker = "RUN 1"
else if str(lat) = "41.354003":
	milemarker = "RUN 2"
else if str(lat) = "41.355332":
	milemarker = "RUN 3"
else:
	milemarker = "Invalid Milemarker"


a = "Object " + obj_name + " with status " + status + " at milemarker " + milemarker
print(a)

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a
# execute_unix(w)

# tts using espeak

"""
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a
execute_unix(c)

#if you can modulate using the mic, you could retrans out the received information
host = '127.0.0.1'
port = 8000

def send_to_server(host, port):
	HOST = host
	PORT = port
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((HOST, PORT))
	server_socket.listen(10)
	print("Listening")
	s = server_socket.accept()
	print("Connected")
"""
