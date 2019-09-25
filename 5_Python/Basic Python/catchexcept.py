
def getInfo():
    while True:
        try:
            var1 = int( input("Please provide the first integer: ") )
            var2 = int( input("Please provide the second integer: ") )
            break
        except ValueError as e:
            print( "\nUnable to convert input to integer:\n{}\n".format(e) )
            continue
        except:
            # if above exception isn't caught
            print("\nUnknown error\n")
            continue
        finally:
            # this will run regardless of the try or except
            print("-------------------------------------------")
            
    print("\n{} + {} = {}\n".format( var1, var2, compute(var1, var2) ) )
          
def compute(var1, var2):
    return var1 + var2


if __name__ == "__main__":
    getInfo()
