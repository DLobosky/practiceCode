#!/usr/bin/python

import getpass
import json
from Tkinter import *
import time

#str = raw_input("Enter input: ");

#print "Received input is: ", str

#print("---------------------------------------")

#test = open("input_file.txt", "a+")
#print "Name of File: ", test.name
#print "Opening Mode: ", test.mode
#print "Is it closed? ", test.closed

#print("---------------------------------------")

#uKey = getpass.getpass('Scan your card!')

#print "Your key number is: ", uKey

#test.write(str(uKey) + "\n")


#-------------------------------------------------------

#master = Tk()
#e = Entry(master)
#e.pack()

#e.focus_set()

#def callback():
#	print e.get() #testyou may want to use later

#b = Button(master, text = "Enter", width = 10, comman = callback)
#b.pack()

#mainloop()

#----------------------------------------------------

root = Tk()

label1 = Label(root, text = "This is a test!", fg="red",bg="black", font=("Helvetica", 16))
label1.pack()

root.after(2000, lambda: root.destroy())
root.mainloop()

