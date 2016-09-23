from Tkinter import *
import Pmw
import serial
import parase

import sys
sys.modules['Pmw']

class Dummy: pass
var = Dummy()

class OE:
    filename = None
    folder = None
    listbox = None
    status_busy = None
    List_button_value=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    button_value= None
    selectPort = None

    ser = serial.Serial(port=selectPort, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=0)
    def check_sum(msg):
        if not msg:
            return None
        s = int( ord(msg[0]) )
        for v in msg[1:]:
            vi = int( ord(v) )
            s = s ^ vi
        return s

    def append_checksum(msg):
        c = check_sum(msg)
        return "%s%x"%(msg,c)

    def onclick(self,i):
       if i<=9:
           print 'clicked ',i
           if self.List_button_value[i-1] == 0:
              self.ser.write(self.append_checksum('$1%d000'% i))
              self.List_button_value[i-1]=1
           elif self.List_button_value[i-1]==1:
              self.ser.write(self.append_checksum('$2%d000'% i))
              self.List_button_value[i-1]=0
       else:
           if self.List_button_value[i-1] == 0:
               print (self.append_checksum('$1%X000' % i))
               self.ser.write(self.append_checksum('$1%X000' % i))
               self.List_button_value[i-1] = 1
           elif self.List_button_value[i-1] == 1:
               self.ser.write(self.append_checksum('$2%X000' % i))
               self.List_button_value[i-1] = 0



    def choseEntry(self,portNum):
        print 'Port:' + portNum
        self.target.configure(text = portNum)
        global selectPort
        selectPort = portNum
        print 'Selected port:' + selectPort
        pass

    def create_button(self,frame, id):
        pass

    def main(self):
        root = Tk()
        root.title('ASTRI')
        Pmw.initialise(root)
        root.geometry('{}x{}'.format(400,150))
        choice = None

        self.target = Label(root,
            relief = 'sunken',
                    padx = 20,
                    pady = 20,
        )


        fm1 = Frame(root)
        fm2 = Frame(root)
        fm3 = Frame(root)
        fm4 = Frame(root)
        fm5 = Frame(root)

        ports = parase.serial_ports()
        combobox = Pmw.ComboBox(fm1, label_text='Select Serial Port:', labelpos='we',
                        listbox_width=10, dropdown=1,
                        selectioncommand=self.choseEntry,
                        scrolledlist_items=ports)
        combobox.pack(side=TOP)
        first = ports[0]
        combobox.selectitem(first) #select com port
        self.choseEntry(first)


        global selectPort
        ser = serial.Serial(port=selectPort, baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS, timeout=0)

        label_text = ''
        for i in range(0,2):
            if i == 0:
                for j in range(1,9):
                    label_text = 'LED0'
                    label_text += str(j)
                    setattr(var, label_text, IntVar())
                    if j < 5:
                        Checkbutton(fm2, text=label_text, state=NORMAL, anchor=W,command=lambda  x=j: self.onclick(x),variable = getattr(var, label_text)).grid(row=i, column=j, sticky=W)
                        #Checkbutton.bind("<button-1>", self.onclick(j))
                    else:
                        Checkbutton(fm3, text=label_text, state=NORMAL, anchor=W,command=lambda x=j: self.onclick(x),variable = getattr(var, label_text)).grid(row=i, column=j, sticky=W)
                        #Checkbutton.bind("<button-1>", self.onclick(j))
            else:
                for j in range(9,17):
                    if j < 10:
                        label_text = 'LED0'
                        label_text += str(j)
                        setattr(var, label_text, IntVar())
                        Checkbutton(fm4, text=label_text, state=NORMAL,anchor=W,command=lambda x=j: self.onclick(x),variable = getattr(var, label_text)).grid(row=i, column=j-9, sticky=W)
                        #Checkbutton.bind("<button-1>", self.onclick(j))
                    else:
                        label_text = 'LED'
                        label_text += str(j)
                        setattr(var, label_text, IntVar())
                        if j < 13:
                            Checkbutton(fm4, text=label_text, state=NORMAL, anchor=W,command=lambda x=j: self.onclick(x), variable=getattr(var, label_text)).grid(row=i, column=j-9, sticky=W)
                        else:
                            Checkbutton(fm5, text=label_text, state=NORMAL, anchor=W,command=lambda x=j: self.onclick(x), variable=getattr(var, label_text)).grid(row=i, column=j - 9, sticky=W)

        fm1.pack(side=TOP,  expand=NO);
        fm2.pack(side=TOP,  expand=NO);
        fm3.pack(side=TOP,  expand=NO);
        fm4.pack(side=TOP,  expand=NO);
        fm5.pack(side=TOP,  expand=NO);
        root.mainloop()

if __name__ == '__main__':
       OE().main()
