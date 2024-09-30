# define the tuple

Weird = ("hello", 10, "goodbye" , 3, "goodnight" , 5, "Go away")

#Get input from the user
userVal = "gabby"

#Weird.append[7] = userVal
            
#try:
#    Weird.append(userVal)
#except AttributeError as e:
#    print(f"Error: You can not append to a tuple. The exception is: {e}")

#Weird = Weird + (userVal,)

#print("New tuple", Weird)

# Use the unpacking operator * to append the new value to the tuple
#Weird = (*Weird, userVal)
#print("New tuple using unpacking operator:", Weird)

#Convert tuple to the list
Weird_list = list(Weird)

# Append the value "Gabby" to the list 
Weird_list.append(userVal)

#Convert the list to a tuple
Weird = tuple(Weird_list)

# Print the new tuple
print("New tuple after appending 'gabby':", Weird)
