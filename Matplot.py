import time
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np

class Plot:
    def __init__(self,master):
        self.master = master
        self.figure = Figure(figsize=(10,8), dpi=100)
        self.figure.subplots_adjust(bottom=0.07, left=0.07, right=0.95, top=0.95)
        self.a = self.figure.add_subplot(1,1,1)
        #Coordinate setup
        self.a.grid(True) #show grid
        self.a.set_title("Realtime Plot")
        self.a.set_xlabel("X Axis")
        self.a.set_ylabel("Y Axis")
        self.a.xaxis.set_ticks(np.arange(0, 1+0.1, 1)) #setup intervals of coordinate
        self.a.yaxis.set_ticks(np.arange(0, 1+0.1, 1))
        #canvas setup
        self.canvas = FigureCanvasTkAgg(self.figure, master = master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        #navigation toolbar setup
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, master)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    def setCoordinate(self,graphsize):
        self.a.grid(True) #show grid
        self.a.set_title("Realtime Plot")
        self.a.set_xlabel("X Axis")
        self.a.set_ylabel("Y Axis")
        self.a.xaxis.set_ticks(np.arange(0, graphsize+0.1, 1)) #setup intervals of coordinate
        self.a.yaxis.set_ticks(np.arange(0, graphsize+0.1, 1))
        self.canvas = FigureCanvasTkAgg(self.figure, master = self.master)
        self.canvas.show()

    def clearGraph(self):
        self.a.clear()
        self.a.grid(True) #show grid
        self.a.set_title("Realtime Plot")
        self.a.set_xlabel("X Axis")
        self.a.set_ylabel("Y Axis")

    def plotLocation(self,graphsize,xList,yList):
        self.a.plot(xList,yList,'ro')
        self.a.xaxis.set_ticks(np.arange(0, graphsize+0.1, 1)) #setup intervals of coordinate
        self.a.yaxis.set_ticks(np.arange(0, graphsize+0.1, 1))

    def showGraph(self):
    	self.canvas.show()