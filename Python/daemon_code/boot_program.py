#!/bin/env python

from Tkinter import *

#os.chdir(/home/dalton/Documents/Python\ Practice/)


test = open("YOU_DID_IT.txt", "a+")

test.write("(11/17/2016)" + "\n")

test.close();

#------------------------------------------------


#root = Tk()

#label1 = Label(root, text = "This is a test!", fg="red", font=("Helvetica", 16))
#label1.pack()

#root.after(2000, lambda: root.destroy())
#root.mainloop()
