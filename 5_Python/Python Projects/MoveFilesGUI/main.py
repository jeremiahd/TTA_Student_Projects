# Step 123
# Jeremiah Davis

import tkinter
import tkinter.filedialog
from tkinter import *
import os
import sqlite3
import shutil
import time

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable( width=False, height=False)
        self.master.geometry( "{}x{}".format(550, 150) )
        self.master.title("Step 123")

        self.fromDir = ""
        self.toDir = ""

        # MOVE FROM DIRECTORY
        self.browseFr = Button( self.master, width=12, text="Move From...",
                                command=lambda:fromDir(self) )
        self.browseFr.grid( row=0, column=0, pady=(40,0), padx=(20,10) )

        self.textFr = Text( self.master, height=1, width=50 )
        self.textFr.grid( row=0, column=1, pady=(40,0) )
        # END MOVE FROM

        # MOVE TO DIRECTORY
        self.browseTo = Button( self.master, width=12, text="Move To...",
                                command=lambda:toDir(self) )
        self.browseTo.grid( row=1, column=0, pady=(15,0), padx=(20,10) )

        self.textTo = Text( self.master, height=1, width=50 )
        self.textTo.grid( row=1, column=1, pady=(15,0) )
        # END MOVE TO

        #EXECUTE
        self.exec = Button( self.master, width=12, text="Execute",
                            command=lambda:execute(self), fg="red" )
        self.exec.grid( row=2, column=1, pady=(5,0), sticky=S+E)
        #END EXECUTE

def fromDir(self):
    self.fromDir = filedialog.askdirectory(initialdir = ".", title="Move FROM",
                                           mustexist=True)
    self.textFr.delete("1.0", END)
    self.textFr.insert("1.0", self.fromDir)

def toDir(self):
    self.toDir = filedialog.askdirectory(initialdir = ".", title="Move FROM",
                                         mustexist=True)
    self.textTo.delete("1.0", END)
    self.textTo.insert("1.0", self.toDir)

def execute(self):
    #make sure there is a directory set in each textbox, and that they're different
    if self.fromDir=="" or self.toDir=="": return
    if self.fromDir == self.toDir: return

    path = self.fromDir
    files = os.listdir(path)
    createDB()
    for file in files:
        fileExt = os.path.splitext(file)[1]
        fullPath = os.path.join(path, file)
        lastMod = os.path.getmtime(fullPath)

        #it's not clear in the instructions if only .txt should be recorded in the
        #db and/or moved with shutil, or all files...this 'if' block can be extended
        #to the rest of this function's logic if the former is the case
        if fileExt == ".txt":
            displayMod = time.strftime( "%m-%d-%Y %H:%M:%S", time.localtime(lastMod) )
            print( "{} - {}".format(fullPath, displayMod) )
        
        db = sqlite3.connect("files.db")
        with db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO files\
                            (fqname, lastMod)\
                            VALUES\
                            ('"+fullPath+"', '"+str(lastMod)+"')")
            
        shutil.move(fullPath, self.toDir)

    print("Exectution Complete")
    self.textFr.delete("1.0", END)
    self.textTo.delete("1.0", END)
        

def createDB():
    db = sqlite3.connect("files.db")
    with db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS files(\
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        fqname TEXT,\
                        lastMod TIMESTAMP)")
        db.commit()
        

if __name__ == "__main__":
    tk = tkinter.Tk()
    window = ParentWindow(tk)
    tk.mainloop()
