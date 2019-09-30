import os
import tkinter
from tkinter import *
import tkinter.messagebox
import sqlite3
import main
import gui

def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if tkinter.messagebox.askokcancel("Exit program", "Okay to exit aplication?"):
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect("phonebook.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS phonebook(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            fname TEXT,\
            lname TEXT,\
            fullname TEXT,\
            phone TEXT,\
            email TEXT);")

        conn.commit()
    #with already calls close() on __exit__(), every video makes a point of memory leaks here
    #but 'with' is syntactic sugar for finally: close() !!!
    first_run(self)

def first_run(self):
    conn = sqlite3.connect("phonebook.db")
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO phonebook\
                (fname, lname, fullname, phone, email)\
                VALUES\
                ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com')")
            conn.commit()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM phonebook""")
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect("phonebook.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT fname, lname, phone, email FROM phonebook WHERE fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])

def addToList(self):
    fname = self.txt_fname.get().strip().title()
    lname = self.txt_lname.get().strip().title()
    fullname = "{} {}".format(fname, lname)
    print("fullname: {}".format(fullname))
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    if not "@" or not "." in email:
        print("Incorrect email format!!!")
    if( len(fname)>0 and len(lname)>0 and len(phone)>0 and len(email)>0):
        conn = sqlite3.connect("phonebook.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(fullname) FROM phonebook WHERE fullname = '{}'""".format(fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO phonebook\
                    (fname, lname, fullname, phone, email)\
                    VALUES(?,?,?,?,?)""",(fname, lname, fullname, phone, email))
                self.list.insert(END, fullname)
                onClear(self)
            else:
                tkinter.messagebox.showerror("Name Error", "'{}' already exists in the database! Please choose a different name.".format(fullname))
                onClear(self)
        conn.commit()
    else:
        tkinter.messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")


def onDelete(self):
    #I stopped typing from the video when I couldn't see it...in the video there is code to actually delete
    #the record from the db, but it doesn't exist in the .zip version I can read...so I added this instead
    fname = self.txt_fname.get().strip().title()
    conn = sqlite3.connect("phonebook.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM phonebook WHERE fname='"+fname+"'")
        conn.commit()
    # end mybrain
        
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    try:
        index = self.list.curselection()[0]
        self.list.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    

def onRefresh(self):
    self.list.delete(0, END)
    conn = sqlite3.connect("phonebook.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT fullname FROM phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.list.insert(0, str(item))
                i = i+1

def onUpdate(self):
    try:
        select = self.list.curselection()[0]
        value = self.list.get(select)
    except:
        tkinter.messagebox.showinfo("Missing selection", "No name was selected from the list box. \nCancelling the update request.")
        return
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    if(len(phone)>0 and len(email)>0):
        conn = sqlite3.connect("phonebook.db")
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(phone) FROM phonebook WHERE phone = '{}'""".format(phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(email) FROM phonebook WHERE email = '{}'""".format(email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:
                response = tkinter.messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?.".format(phone, email, value))
                print(response)
                if response:
                    cur.execute("""UPDATE phonebook SET phone = '{0}', email = '{1}' WHERE fullname = '{2}'""".format(phone,email,value))
                    onClear(self)
                    conn.commit()
                else:
                    tkinter.messagebox.showinfo("Cancel request", "No changes have been made to ({}).".format(value))
            else:
                tkinter.messagebox.showinfo("No changes detected", "Both ({}) and ({})\n already exist in the database for this name. \n\n Your update request has been cancelled.".format(phone, email))
            onClear(self)
    else:
        tkinter.messagebox.showerror("Missing information", "Please select a name from the list. \n Then edit the phone or email information.")
        onClear(self)

if __name__ == "__main__":
    pass
                

        
                    
        
