#!/usr/bin/python

import RPi.GPIO as GPIO

port_str = input('Select the port: ')
port = int(port_str)

GPIO.setmode(GPIO.BOARD) # pin GPIO
GPIO.setup(port, GPIO.OUT) # salida

p = GPIO.PWM(port, 1300) # channel=12 frequency=800->derecha frecuencia=1300->parado frecuencia=2200->izquierda
p.start(50) # duty cycle debe ser 50%

r = input('Press return to stop: ')   # use raw_input for Python 2

p.stop()
GPIO.cleanup()
