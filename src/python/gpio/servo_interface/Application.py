#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Application.py
#
#       Copyright 2014 Raul Perula-Martinez <raul.perula@uc3m.es>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.

from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style, Entry
import Motor

class Application(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        # size
        self.width = 250
        self.height = 120

        # screen size
        self.sw = self.parent.winfo_screenwidth()
        self.sh = self.parent.winfo_screenheight()

        # create a Motor object
        self.motor = Motor()

        # init UI and centering in the screen
        self.initUI()
        self.centering()

    def initUI(self):
        self.parent.title("RPI Motors")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # configure grid
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)

        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)

        # label
        self.port_lbl = Label(self, text="Port")
        self.port_lbl.grid(row=0, column=0, pady=4, padx=5, sticky=W+E)

        # input text
        self.entry = Entry(self, )
        self.entry.grid(row=0, column=1, columnspan=3, sticky=W+E)

        # control buttons
        self.cls = Button(self, text="Turn Left", command=self.motor.turn_left())
        self.cls.grid(row=1, column=0, sticky=E+W)
        self.bck = Button(self, text="Stop", command=self.motor.stop_mov())
        self.bck.grid(row=1, column=1, sticky=E+W)
        self.lbl = Button(self, text="Turn Right", command=self.motor.turn_right())
        self.lbl.grid(row=1, column=2, sticky=E+W)

        # exit button
        self.clo = Button(self, text="Exit", command=self.quit)
        self.clo.grid(row=2, columnspan=4, sticky=E+W)

        # draw
        self.pack()

    def centering(self):
        self.posX = (self.sw - self.width) / 2
        self.posY = (self.sh - self.height) / 2

        self.parent.geometry('%dx%d+%d+%d' % (self.width, self.height, self.posX, self.posY))

    def set_new_port():
        self.motor.set_port(self.entry.get())

def main():

    root = Tk()

    app = Application(root)

    root.mainloop()


if __name__ == '__main__':
    main()
