from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

def cbClicked():
	print 'click!'
	CheckVar1 = C1.select()
	print CheckVar1
	#if Checkbutton.select() == True:
	#	print '1111'
	#else:
	#	print '0000'

C1 = Checkbutton(top, text = "Music", command = cbClicked,variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

C1.pack()
C2.pack()
top.mainloop()