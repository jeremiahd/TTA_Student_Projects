import sqlite3

db = sqlite3.connect("test.db")

#python docs say __exit__() closes the file..."with" is syntactic sugar
#for try blocks that use finally: close()...calling close() is redundant
with db:
    cursor = db.cursor()
    #no need for redundant tbl_ or col_ nomenclatures...I know when I'm
    #accessing a table or column...there is no confusion to be solved
    cursor.execute("CREATE TABLE IF NOT EXISTS persons(\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    fname TEXT,\
                    lname TEXT,\
                    email TEXT)")
    db.commit()


"""
db = sqlite3.connect("test.db")
with db:
    cursor = db.cursor()
    #we can use the same insert statement for multiple records
    cursor.execute("INSERT INTO persons\
                    (fname, lname, email)\
                    VALUES\
                    ('jeremiah', 'davis', 'jeremiahd@gmail.com'),\
                    ('bob', 'smith', 'bob@smith.com')")
    db.commit()
"""

db = sqlite3.connect("test.db")
with db:
    cursor = db.cursor()
    results = cursor.execute("SELECT * FROM persons WHERE fname = 'bob'")
    #results = cursor.fetchall() #this can be used as well
    db.commit()
    for result in results:
        #print(result) # useful to see entire record
        #print every 'result'
        print( "First Name: {}\nLast Name: {}\nEmail: {}"\
               .format(result[1], result[2], result[3]) )


#so I can play around with the table and reset it
"""
db = sqlite3.connect("test.db")
with db:
    cursor = db.cursor()
    cursor.execute("DELETE FROM persons")
    db.commit()
"""
    
