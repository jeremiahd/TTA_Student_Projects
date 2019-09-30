import tkinter
from tkinter import *
import main
import func

def load(self):
    self.lbl_fname = tkinter.Label(self.master, text="First Name:")
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tkinter.Label(self.master, text="Last Name:")
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tkinter.Label(self.master, text="Phone Number:")
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tkinter.Label(self.master, text="Email Address:")
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_user = tkinter.Label(self.master, text = "User:")
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

    self.txt_fname = tkinter.Entry(self.master, text="")
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_lname = tkinter.Entry(self.master, text="")
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_phone = tkinter.Entry(self.master, text="")
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_email = tkinter.Entry(self.master, text="")
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)

    self.scroll = tkinter.Scrollbar(self.master, orient=VERTICAL)
    self.list = tkinter.Listbox(self.master, exportselection=0, yscrollcommand=self.scroll.set)
    self.list.bind("<<ListboxSelect>>", lambda event: func.onSelect(self, event))
    self.scroll.config(command=self.list.yview)
    self.scroll.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.list.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    self.btn_add = tkinter.Button(self.master, width=12, height=2, text="Add", command=lambda:func.addToList(self))
    self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky=W)
    self.btn_update = tkinter.Button(self.master, width=12, height=2, text="Update", command=lambda:func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky=W)
    self.btn_delete = tkinter.Button(self.master, width=12, height=2, text="Delete", command=lambda:func.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky=W)
    self.btn_close = tkinter.Button(self.master, width=12, height=2, text="Close", command=lambda:func.ask_quit(self))
    self.btn_close.grid(row=8, column=4, columnspan=1, padx=(15,0), pady=(45,10), sticky=E)

    func.create_db(self)
    func.onRefresh(self)


if __name__ == "__main__":
    pass
    
    
