import time
from random import randint

from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import Matplot

import Serialport
import serial

import threading
import Threads
import collections

# Class for Draw tables
class Table(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('X Coordinate', 'Y Coordinate', 'Differential Voltage 1',
            'Differential Voltage 2','Differential Voltage 3','Differential Voltage 4')
        tv.heading("#0", text='Date&Time', anchor='w')
        tv.column("#0", anchor="w",width = 100)
        tv.heading('X Coordinate', text='X Coordinate')
        tv.column('X Coordinate', anchor='center', width=100)
        tv.heading('Y Coordinate', text='Y Coordinate')
        tv.column('Y Coordinate', anchor='center', width=100)
        tv.heading('Differential Voltage 1', text='Differential Voltage 1')
        tv.column('Differential Voltage 1', anchor='center', width=100)
        tv.heading('Differential Voltage 2', text='Differential Voltage 2')
        tv.column('Differential Voltage 2', anchor='center', width=100)
        tv.heading('Differential Voltage 3', text='Differential Voltage 3')
        tv.column('Differential Voltage 3', anchor='center', width=100)
        tv.heading('Differential Voltage 4', text='Differential Voltage 4')
        tv.column('Differential Voltage 4', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', '0', text="Example", values=('x',
                             'y', 'z', 'u', 'v', 'w'))
# Class for Buttons 
class Widgets:
    graphsize = 10
    def __init__(self,master):
        self.master = master
        self.box_value = StringVar()
        self.connection = False
        self.sizeofgraph = StringVar()
        self.sizeofgraph = "Default Size is 10 Meters!"
        self.connectionstatus = StringVar()
        self.connectionstatus = "Serial Port is Not Connected!"
        #Change the name of the title
        master.wm_title("Vector Mapping 0.1 - SMT Research Ltd.")
        #Define all buttons
        self.button_1 = Button(master, text = "Start", font = ("comic sans ms",20)) #, font = ("comic sans ms",25)
        self.button_2 = Button(master, text = "Stop", font = ("comic sans ms",20))
        self.button_3 = Button(master, text = "Confirm")
        self.button_4 = Button(master, text = "Up")
        self.button_5 = Button(master, text = "Down")
        self.button_6 = Button(master, text = "Left")
        self.button_7 = Button(master, text = "Right")
        self.button_8 = Button(master, text = "Rescan")
        self.button_9 = Button(master, text = "Connect")
        self.button_10 = Button(master, text = "Activate") #, font = ("comic sans ms",25)
        self.button_11 = Button(master, text = "Cancel")
        self.label_1 = Label(master, text = "Set Height&Width(m)",bg ='white', font = ("comic sans ms", 15, "bold"))
        self.label_2 = Label(master, text = "Manual Control Panel",bg ='white', font = ("comic sans ms", 15, "bold"))
        self.label_3 = Label(master, text = "Serial Port Select",bg ='white', font = ("comic sans ms", 15, "bold"))
        self.label_4 = Label(self.master, text = self.connectionstatus, font = ("Helvetica", 12, "italic"))
        self.label_5 = Label(self.master, text = self.sizeofgraph, font = ("Helvetica", 12, "italic"))
        self.entry_1 = Entry(master)
        self.box = Combobox(master, textvariable = self.box_value, state ='readonly')
        self.box['values'] = Serialport.serial_Ports()
        self.box.current(0)
        #Bind all widgets to functions
        self.button_1.bind("<Button-1>",self.bindingStart)
        self.button_2.bind("<Button-1>",self.bindingStop)
        self.button_3.bind("<Button-1>",self.bindingConfirm)
        self.button_4.bind("<Button-1>",self.bindingUp)
        self.button_5.bind("<Button-1>",self.bindingDown)
        self.button_6.bind("<Button-1>",self.bindingLeft)
        self.button_7.bind("<Button-1>",self.bindingRight)
        self.button_8.bind("<Button-1>",self.bindingRescan)
        self.button_9.bind("<Button-1>",self.bindingConnect)
        self.button_10.bind("<Button-1>",self.bindingActivate)
        self.button_11.bind("<Button-1>",self.bindingCancel)
        self.master.bind("<Left>", self.bindingLeft)
        self.master.bind("<Right>", self.bindingRight)
        self.master.bind("<Up>", self.bindingUp)
        self.master.bind("<Down>", self.bindingDown)

        # Grid Layout for all wigets
        # Start and Stop button layout
        self.button_1.grid(row = 0, rowspan = 2, column = 81, ipadx = 10, sticky = W+E+N+S) #Start button,ipadx = 20, ipady = 20 , rowspan = 9, sticky = W+E+N+S
        self.button_2.grid(row = 0, rowspan = 2,column = 82,ipadx = 10, sticky = W+E+N+S) #Stop button, ipadx = 20, ipady = 20 , rowspan = 9 , sticky = W+E+N+S
        #Set Height and Width Layout
        self.label_1.grid(row = 10, column = 81, columnspan = 2, sticky = S) #Height&Width Label
        self.entry_1.grid(row = 11, column = 81, columnspan = 2) #Blank space Entry
        self.label_5.grid(row = 12, column = 81, columnspan = 2, sticky = N)
        self.button_3.grid(row = 13, column = 81, columnspan = 2) #Confirm button
        #Serial Port Select
        self.label_3.grid(row = 20, column  = 81, columnspan = 2, sticky = S) #Serial Port Select
        self.box.grid(row = 21, column = 81, columnspan = 2) #Combobox for serial ports
        self.label_4.grid(row = 22, column = 81, columnspan = 2, sticky = N) #connection message
        self.button_8.grid(row = 23, column = 81, sticky = E) #Rescan Button
        self.button_9.grid(row = 23, column = 82, sticky = W) #Connect Button
        #Control Panel Layout
        self.label_2.grid( row = 50, column = 81, columnspan = 2, sticky = S) #Manual Control Panel Label
        self.button_10.grid(row = 52, column = 81, sticky = W+E+N+S) 
        self.button_11.grid(row = 52,column = 82, sticky = W+E+N+S)
        self.button_4.grid(row = 54, column = 81, columnspan = 2) #Up button
        self.button_6.grid(row = 55, column = 81) #Left Button
        self.button_7.grid(row = 55, column = 82) #Right Button
        self.button_5.grid(row = 56, column = 81, columnspan = 2) #Down Button
        self.master.update()
    #Binding Functions
    def bindingStart(self,event):
        if self.connection :
            global start 
            start = True
            listener.write(b'Start')
            global thread 
            thread = checkVariables()
            thread.start()
        else :
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
    def bindingStop(self,event):
        try:
            self.connectionstatus = "Serial Port is not Connected :)"
            self.label_4.config(text = self.connectionstatus, font = ("Helvetica", 12, "italic"))
            if listener is None or thread is None:
                self.connection = False
                pass
            else:
                listener.write(b'Stop')
                self.connection = False
                global start
                start = False
                thread.stopit()
                thread.join()
        except (OSError, serial.SerialException):
            print("OSError")
    def bindingConfirm(self,event):
        entry = self.entry_1.get()
        if entry.isdigit():
            if int(entry) <= 10 and int(entry) >= 0:
                # print("Binding Confirm is sucessful too, and the string in the Entry is " + entry)
                if self.connection:
                    listener.write(bytes(entry, 'UTF-8'))
                    self.sizeofgraph = "Size Has Been Set to " + str(entry) +" Meters!"
                    self.label_5.config(text = self.sizeofgraph, font = ("Helvetica", 12, "italic"))
                else:
                    tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
                self.entry = int(entry)
                self.graphsize = int(entry)
                # Tabs(self.master).clearGraph()
                # # Tabs(self.master).setCoordinate(self.entry)
            else:
                tkinter.messagebox.showinfo("Illegal Input", "Number has to be larger than 0 meter and smaller than 10 meters")
        else:
            tkinter.messagebox.showinfo("Illegal Input", "Input has to be a number")
    def bindingActivate(self,event):
        if self.connection:
            listener.write(b'Activate')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Activate is sucessful too")
    def bindingCancel(self,event):
        if self.connection:
            listener.write(b'Cancel')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Cancel is sucessful too")
    def bindingUp(self,event):
        if self.connection:
            listener.write(b'Up')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Up is sucessful too")
    def bindingDown(self,event):
        if self.connection:
            listener.write(b'Down')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Down is sucessful too")
    def bindingLeft(self,event):
        if self.connection:
            listener.write(b'Left')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Left is sucessful too")
    def bindingRight(self,event):
        if self.connection:
            listener.write(b'Right')
        else:
            tkinter.messagebox.showinfo("No Connection", "Serial port has not been connected yet :(")
        # print("Binding Right is sucessful too")
    def bindingRescan(self,event):  #update available serial ports
        self.box['values'] = Serialport.serial_Ports()
    def bindingConnect(self,event):
        self.portname = self.box.get()
        try:
            self.error = False
            self.message =  Serialport.serial_Setup(self.portname)
        except (OSError, serial.SerialException):
            tkinter.messagebox.showinfo("OSError", "The connection is failed！Please double check the connection :(")
            self.connectionstatus = "Serial Port is Not Connected :("
            self.label_4.config(text = self.connectionstatus, font = ("Helvetica", 12, "italic"))
            self.error = True
            self.connection = False
        if self.error:
            pass
        else:
            self.connectionstatus = "Serial Port is Connected :)"
            self.label_4.config(text = self.connectionstatus, font = ("Helvetica", 12, "italic"))
            self.connection = True
            global listener
            listener = self.message

class Tabs:
    def __init__(self,master):
        #notebook(tabs) created
        self.notebook = Notebook(master)
        self.frame_1 = Frame(self.notebook)
        self.frame_2 = Frame(self.notebook)
        self.notebook.add(self.frame_1, text='Vector Map')
        self.notebook.add(self.frame_2, text='Show Raw Data')
        self.notebook.grid(row = 0, rowspan = 81, columnspan = 80, sticky = N+W)

        self.plot = Matplot.Plot(self.frame_1)

        #Embed a table into tkinter
        self.table = Table(self.frame_2)

    #function to insert a piece of Raw Data
    def loadData(self, master, time, x, y, df1, df2, df3, df4):
        self.table.treeview.insert('', '0', text = time, values = (x,
                                     y, df1, df2, df3, df4))
        master.update()

    def plotLocation(self,graphsize,xList,yList):
        self.plot.clearGraph()
        self.plot.plotLocation(graphsize,xList,yList)
        self.plot.showGraph()

    def setCoordinate(self,graphsize):
        self.plot.setCoordinate(graphsize)

    def clearGraph(self):
        self.plot.clearGraph()

class checkVariables(Threads.StoppableThread):
    global xList
    global yList
    def __init__(self):
       Threads.StoppableThread.__init__(self)
       print( "thread init") 
    def run(self):
        print( "thread running" )
        while not self.stopped():
            if start :
                Serialport.serial_Start(listener,xList,yList)
                # print(xList)
                # print(yList)
                if (len(xList)>=1):
                    a = randint(0,10)
                    b = randint(0,10)
                    xcoordinate = xList[len(xList)-1]
                    ycoordinate = yList[len(yList)-1]
                    time = "Time Stamp " + str(len(xList))
                    if  time in date:
                        pass
                    else:
                        date.append(time)
                        if(start):
                            tabs.loadData(root, time, xcoordinate, ycoordinate, a+1,b+1, b+2, a+2)
                    if (start):
                        tabs.plotLocation(widgets.graphsize,xList,yList)
        print( "thread ending" )

def main():
    global root
    root = Tk()
    global widgets
    widgets = Widgets(root)
    global tabs
    tabs = Tabs(root)
    root.mainloop()

if __name__ == '__main__':
    start = False
    listener = None
    thread = None
    root = None
    tabs = None
    widgets = None
    xList = []
    yList = []
    date = []
    main()
