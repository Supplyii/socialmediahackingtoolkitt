from tkinter import *
import pyautogui as gui
import tkinter
import os
import easygui

class ABC(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel().title("Instagram brute force 2022")

        # this adds something to the frame, otherwise the default
        # size of the window will be very small

