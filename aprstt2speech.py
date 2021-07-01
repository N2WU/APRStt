#!/usr/bin/python3
#
#
# Text-to-speech using Direwolf APRS Touchtone variables
# Coincides with custom APRS Direwolf config file
#
# Nolan Pearce, N2WU
#https://pythonbasics.org/text-to-speech/

import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output


#we only need to edit and adjust "a"

obj_name = TTCALL
status = TTSTATUS
lat = TTLAT
lon = TTLON

a = "Object" + obj_name + "with status" + status + "at latitude" + lat + "and longitutde" + lon

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)

#if you can modulate using the mic, you could retrans out the received information
