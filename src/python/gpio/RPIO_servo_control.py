#!/usr/bin/python

# Manteiner Raul
# Version 1.2
# From V1.1
# Usage:
#       $ sudo python servocontrol.py
#       or
#       $ sudo ./servocontrol.py
# Send commands to servo to turn right or
# left specific time(0.2 sec) it is possible stop the servo.
# check the interface to more info.

from RPIO import PWM
import time

servo = PWM.Servo()

stop = 1460
turn_left = 2200
turn_right = 1200

port = 18
print 'GPIO PORT 18 (BOARD PIN 12)\n'

selection = float('inf')
while selection != 0:
	print "\n0 - Quit"
	print "1 - Turn left"
	print "2 - Turn right\n"
	
	selection = raw_input("Input: \n")
	if len(selection) == 0:
		selection = float('inf')
	else:
		selection = int(selection)
	
	if selection == 1:
		freq = turn_left
	elif selection == 2:
		freq = turn_right
	else:
		freq = stop
		
	servo.set_servo(port, freq)
	time.sleep(0.2)
	servo.stop_servo(port)

# stop servo when quit
servo.stop_servo(port)
