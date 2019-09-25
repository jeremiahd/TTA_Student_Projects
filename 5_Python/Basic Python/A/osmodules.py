import os

#fName = "Hello3.txt"
#fPath = "C:/Users/House/Desktop/TTA/5_Python/Basic Python/A/"

def readFile(fName):
    fPath = os.getcwd()
    fullPath = os.path.join(fPath, fName)
    try:
        with open(fullPath) as f:
            print(f)
            print( f.read() )
    except Exception as e:
        print( "Unable to open file:\n {}, in:\n {},\n system error:\n{}".format(fName, fPath, e) )


if __name__ == "__main__":
    fName = input("File name:")
    readFile(fName)
