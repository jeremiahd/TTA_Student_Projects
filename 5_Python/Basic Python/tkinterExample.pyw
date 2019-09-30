import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable( width = False, height = False )
        self.master.geometry( "{}x{}".format(400, 200) )
        self.master.title( "Learning Tkinter" )
        self.master.config( bg = "lightgray" )
		
        self.fName = StringVar()
        self.lName = StringVar()

        #FIRST NAME LABEL
        self.fName_label = Label( self.master,
            text = "First Name",
            font = ( "Helvetica", 14 ),
            fg = "black",
            bg = "lightgray" )
        self.fName_label.grid( row=0, column=0,
            padx=(15, 10), pady=(20,0) )

        #LAST NAME LABEL
        self.lName_label = Label( self.master,
            text = "Last Name",
            font = ( "Helvetica", 14 ),
            fg = "black",
            bg = "lightgray" )
        self.lName_label.grid( row=1, column=0,
            padx=(15, 10), pady=(3,0) )

        #DISPLAY LABEL
        self.output_label = Label( self.master,
            text = "",
            font = ("Helvetica", 14),
            fg = "black",
            bg = "lightgray" )
        self.output_label.grid( row=3, column=0,
            columnspan="3", padx=(15,0), pady=(30,0) )
        
        #FIRST NAME INPUT
        self.fName_input = Entry( self.master,
            text = "",
            justify = "right",
            font = ("Helvetica", 14),
            fg = "black",
            bg = "lightblue" )
        self.fName_input.grid( row=0, column=1,
            padx=(5, 10), pady=(20,0) )

        #LAST NAME INPUT
        self.lName_input = Entry( self.master,
            text = "",
            justify = "right",
            font = ("Helvetica", 14),
            fg = "black",
            bg = "lightblue" )
        self.lName_input.grid( row=1, column=1,
            padx=(5, 10), pady=(3,0) )

        #BUTTONS
        self.submit_btn = Button( self.master,
            text = "Submit",
            width = 10,
            font = ("Helvetica", 12),
	    command = self.submit )
        self.submit_btn.grid( row= 2, column=1,
            padx=(0, 10), pady=(15,0), sticky=NE )
        
        self.cancel_btn = Button( self.master,
            text = "Cancel",
            width = 10,
            font = ("Helvetica", 12),
            fg="red",
            command = self.cancel )
        self.cancel_btn.grid( row=2, column=1,
            padx=(10, 0), pady=(15,0), sticky=NW )
	

    #SUBMIT BUTTON HANDLER
    def submit(self):
        fName = self.fName_input.get()
        lName = self.lName_input.get()
        self.output_label.config( text="Hello, {} {}!"
            .format(fName, lName) )
        

    #CANCEL BUTTON HANDLER
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    tk = Tk()
    window = ParentWindow(tk)
    tk.mainloop()
