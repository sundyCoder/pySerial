from Tkinter import *
from  tkMessageBox import showerror
import tkFileDialog
import subprocess
import os
import glob
import Pmw
import parase

choice = 0

class Dummy: pass
var = Dummy()


class OE:
    filename = None
    folder = None
    listbox = None
    status_busy = None 

    def changeText(self, text):
        print 'Text: ' + text
        if text:
            global choice
            choice = text

    def serial_connect():
        if parase.connect_serial(port_set=self.choice, baud_rate_set=9600):
            ConnectButton.config(text='connected')
            print "Connected."

    def main(self):
        root = Tk()
        root.title('ASTRI')
        Pmw.initialise()
        root.geometry('{}x{}'.format(400,150))

        fm1 = Frame(root)
        fm2 = Frame(root)
        fm3 = Frame(root)
        fm4 = Frame(root)
        fm5 = Frame(root)

        
        ports = parase.serial_ports()        
        combobox = Pmw.ComboBox(fm1, label_text='Select Serial Port:', labelpos='we',
                        listbox_width=10, dropdown=1,
                        selectioncommand = self.changeText,
                        scrolledlist_items=ports)
        combobox.pack(side=LEFT)        
        first = ports[0]        
        self.changeText(first)
        combobox.selectitem(first) #select com port
        global choice
        print 'Port:' + choice

        ConnectButton = Button(fm1, command=self.serial_connect, text="Connect")
        ConnectButton.pack(side=LEFT)

        label_text = ''
        for i in range(0,2):
            if i == 0:         
                for j in range(1,9):
                    label_text = 'LED0' 
                    label_text += str(j)                            
                    if j < 5:
                        setattr(var, label_text, IntVar())        
                        Checkbutton(fm2, text=label_text, state=NORMAL, anchor=W,variable = getattr(var, label_text)).grid(row=i, column=j, sticky=W)        
                    else:
                        setattr(var, label_text, IntVar())        
                        Checkbutton(fm3, text=label_text, state=NORMAL, anchor=W,variable = getattr(var, label_text)).grid(row=i, column=j, sticky=W)        
            else:
                for j in range(9,17):
                    if j < 10:
                        label_text = 'LED0'
                        label_text += str(j)
                        setattr(var, label_text, IntVar())
                        Checkbutton(fm4, text=label_text, state=NORMAL, anchor=W,variable = getattr(var, label_text)).grid(row=i, column=j-9, sticky=W)        
                    else:
                        label_text = 'LED'
                        label_text += str(j)
                        setattr(var, label_text, IntVar())
                        if j < 13:
                            Checkbutton(fm4, text=label_text, state=NORMAL, anchor=W,variable = getattr(var, label_text)).grid(row=i, column=j-9, sticky=W)        
                        else:
                            Checkbutton(fm5, text=label_text, state=NORMAL, anchor=W,variable = getattr(var, label_text)).grid(row=i, column=j-9, sticky=W)        
        fm1.pack(side=TOP,  expand=NO);
        fm2.pack(side=TOP,  expand=NO);
        fm3.pack(side=TOP,  expand=NO);
        fm4.pack(side=TOP,  expand=NO);
        fm5.pack(side=TOP,  expand=NO);       
        root.mainloop()


if __name__ == '__main__':
    OE().main()
