name = "python" #global scope
def getName():
	name = "c#" #local scope
	print("I am coding with {}".format(name))

getName() #returns "c#"
print("I am coding with {}".format(name)) #returns "python"