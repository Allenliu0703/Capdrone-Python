from GUI import *
from random import randint
import time
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox
from Serialport import *
# def main():
 
#     global root
#     root = Tk()
#     global widgets
#     widgets = Widgets(root)
#     global tabs
#     tabs = Tabs(root)
#     root.mainloop()

if __name__ == '__main__':
    # global start
    # global listener
    # global thread
    # global root
    # global tabs
    # global widgets
    start = False
    listener = None
    thread = None
    root = None
    tabs = None
    widgets = None
    # global xList
    # global yList
    # global date
    xList = []
    yList = []
    date = []
    main()