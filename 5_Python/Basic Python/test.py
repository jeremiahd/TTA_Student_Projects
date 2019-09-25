#function declaration..use indentations and no semicolons
def getSum(num1, num2):
	answer = num1 + num2
	print("The answer is {}.".format(answer))
getSum(2,4)

# are we copying all the code to another space in memory, or assigning
# the pointer 'myAdd' to the exact same instructions?
myAdd = getSum

myAdd(3,4)