import sqlite3
import os
import time

# if our db doesn't exist, create it
def createDb():
    db = sqlite3.connect("files.db")
    with db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS files(\
                        id INTEGER PRIMARY KEY AUTOINCREMENT,\
                        path TEXT,\
                        fName TEXT,\
                        fExt TEXT)")
        db.commit()

# ask our os for all the files in this dir, store .txt names in db
def storeFiles():
    fileData = []
    path = os.getcwd()
    files = os.listdir(path)
    db = sqlite3.connect("files.db")
    with db:
        for file in files:
            fExt = os.path.splitext(file)[1]
            cursor = db.cursor()
            if fExt == '.txt':
                cursor.execute("INSERT INTO files\
                                (path, fName, fExt)\
                                VALUES ('"+\
                                path+"', '"+file+"', '"+fExt+"')")
            db.commit()

# query our db for file data, and display to user
def displayData():
    db = sqlite3.connect("files.db")
    with db:
        cursor = db.cursor()
        results = cursor.execute("SELECT * FROM files")
        for result in results:
            # create FQN only for display, there's no need to store
            # redundant data in our db
            fullPath = os.path.join(result[1], result[2])
            print(fullPath)

# reset the db for testing
def deleteAll():
    db = sqlite3.connect("files.db")
    with db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM files")
        db.commit()
        

if __name__ == "__main__":
    createDb()
    deleteAll()
    storeFiles()
    displayData()
