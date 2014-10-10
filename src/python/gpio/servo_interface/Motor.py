#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Motor.py
#
#       Copyright 2014 Raul Perula-Martinez <raul.perula@uc3m.es>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.

from RPIO import PWM
import time

# basic frequencies
stop = 1460
left = 2200
right = 1200

class Motor():

    def __init__(self):
        global stop

        self.servo = PWM.Servo()

        # default values
        self.freq = stop
        self.port = 18

    def __str__():
        print 'GPIO PORT 18 (BOARD PIN 12)\n'

    def set_port(port):
        self.port = port

    def turn_left():
        global left

        self.freq = left
        self.servo.set_servo(self.port, self.freq)
        time.sleep(0.2)
        self.servo.stop_servo(self.port)

    def turn_right():
        global right

        self.freq = right
        self.servo.set_servo(self.port, self.freq)
        time.sleep(0.2)
        self.servo.stop_servo(self.port)

    def stop_mov():
        self.servo.stop_servo(self.port)
