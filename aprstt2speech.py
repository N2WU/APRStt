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


a = "Object " + obj_name + " with status " + status + " at latitude " + lat + " and longitutde " + lon
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
