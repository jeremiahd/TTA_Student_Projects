import os
import time

if __name__ == "__main__":

    # First, let's get our current path
    path = os.getcwd()

    # Next, let's get a list of files in 'path'
    files = os.listdir(path)

    for file in files:
        # concatenate our full path, and parse out our extension
        fullPath = os.path.join(path, file)
        fileExt = os.path.splitext(file)[1]
        
        # only output .txt files
        if fileExt == ".txt":
            # ask the os when the last modification was, convert to local time, and set the time format
            lastMod = time.strftime( "%m-%d-%Y %H:%M:%S", time.localtime(os.path.getmtime(file)) )
            print( "{} - {}".format(lastMod, fullPath) )
    
