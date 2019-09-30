# Step 121
# Jeremiah Davis

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable( width=False, height=False)
        self.master.geometry( "{}x{}".format(480, 170) )
        self.master.title( "Check Files" )

        #COLUMN 0
        self.browse1 = Button( self.master, width=12, text="Browse..." )
        self.browse2 = Button( self.master, width=12, text="Browse..." )
        self.check = Button( self.master, height=2, text="Check for files..." )

        self.browse1.grid( row=0, column=0, pady=(40,0), padx=(15,10) )
        self.browse2.grid( row=1, column=0, pady=(10,0), padx=(15,10) )
        self.check.grid( row=2, column=0, pady=(10,0), padx=(15,10) )

        #COLUMN 1
        self.text1 = Entry( self.master, text="", width=55 )
        self.text2 = Entry( self.master, text="", width=55 )

        self.text1.grid( row=0, column=1, columnspan=2, pady=(40,0) )
        self.text2.grid( row=1, column=1, columnspan=2, pady=(10,0) )

        #COLUMN 2
        self.close = Button( self.master, height=2, text="Close Program" )
        self.close.grid( row=2, column=2, sticky=S+E )
                              

if __name__ == "__main__":
    tk = tkinter.Tk()
    window = ParentWindow(tk)
    tk.mainloop()
