mySentence = "loves the color"

color_list = ["red", "blue", "green", "pink", "teal", "black"]

def color_function(name):
    msg = []
    for i in color_list:
        msg.append( "{0} {1} {2}".format(name, mySentence, i) )
    return msg


lst = color_function("Jeremiah")

for i in lst:
    print(i)
