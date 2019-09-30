# Python version 3.7.3
# Author: Daniel A. Christie
# Phonebook drill

import tkinter
from tkinter import *
import gui
import func

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        func.center_window(self,500,300)
        self.master.title("Dan's phonebook demo")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol( "WM_DELETE_WINDOW", lambda: func.ask_quit(self) )
        arg = self.master
        gui.load(self)


if __name__ == "__main__":
    root = tkinter.Tk()
    window = ParentWindow(root)
    root.mainloop()
