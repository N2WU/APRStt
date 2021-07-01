# APRStt
Configuration files and setup for the West Point Triathlon using APRS touchtone

**APRStt.conf**

This file is what is inserted into direwolf.conf. It contains all the reporting procedures for the race.

**Commsproc.txt**

This file has the psuedocode and reasons for the code in APRStt.conf. 

**direwolf.conf**

This is the actual direwolf config. It uses the W2KGY callsign, so change it to your own. 

**aprstt2speech.py**

This is a python function that reads callsign/object name, position, and status, then reads it aloud. It uses espeak. It must be referenced in the direwolf.conf file.
