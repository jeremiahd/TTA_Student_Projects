# Step 121
# Jeremiah Davis

import tkinter
import tkinter.filedialog
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable( width=False, height=False)
        self.master.geometry( "{}x{}".format(700, 120) )
        self.master.title( "Check Files" )

        self.browse = Button( self.master, width=12, text="Browse...",
                              command=lambda:browseDir(self) )
        self.browse.grid( row=0, column=0, pady=(40,0), padx=(20,10) )

        self.text = Text( self.master, height=1, width=65 )
        self.text.grid( row=0, column=1, columnspan=2, pady=(40,0) )


def browseDir(self):
    dirName = filedialog.askdirectory(initialdir = ".",title = "Select directory",
                                            mustexist = True)
    self.text.delete("1.0", END)
    self.text.insert("1.0", dirName)

if __name__ == "__main__":
    tk = tkinter.Tk()
    window = ParentWindow(tk)
    tk.mainloop()
