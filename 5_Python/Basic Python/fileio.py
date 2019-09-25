import os

#print(dir(str))
#print(help(str))

"""
print( os.getcwd() )
file = open("test.txt", mode="rb")
print( file.read() )
file.close()
"""

#use with (its like a while?) for better error handling, and file closing

def readFile(fName):
    with open(fName) as f:
        return f.read()

def writeData(fName, data):
    with open(fName, mode="wt") as f:
        f.write(data)

def appendData(fName, data):
    with open(fName, mode="a") as f:
        f.write(data)


if __name__ == "__main__":

    print( readFile("test.txt") )

    writeData("test.txt", "new text in file")
    appendData("test.txt", "weee")

    print(readFile("test.txt") )
