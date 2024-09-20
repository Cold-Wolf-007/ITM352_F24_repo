# Ask the user to enter their first name, middle inital 
# last name. Concaternate them together with spaces in between
# and print out the results

First = input("Please enter your first name: ")
MiddleInitial = input("Please enter the your middle initial")
Last = input("Please enter your last name: ")

FullName = " ".join([First, MiddleInitial, Last])
FullNameList = ([First, MiddleInitial, Last])
print("Your full name is ", FullName)

print("Your full name is {} {} {}".format(First, MiddleInitial, Last))
print("Your full name is {} {} {}".format(*FullNameList))
print(f"Your full name is {First} {MiddleInitial} {Last}")
print("Your full name is %s %s %s" % (First, MiddleInitial, Last))