#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # pin GPIO
GPIO.setup(12, GPIO.OUT) # salida

p = GPIO.PWM(12, 2200) # channel=12 frequency=0.5Hz
p.start(100) # duty cycle (en este caso 50%)

input('Press return to stop:')   # use raw_input for Python 2

p.stop()
GPIO.cleanup()
