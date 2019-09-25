mySentence = "loves the color"

color_list = ["red", "blue", "green", "pink", "teal", "black"]

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    while True:
        name = input("What is your name? ")
        if name == "Sally":
            print("Sally, you may not use this software")
        elif not name == "":
            break
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()
