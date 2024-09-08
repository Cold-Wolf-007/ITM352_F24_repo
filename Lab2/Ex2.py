# Get the user"s birth year and substract the current year to
# get their current age.

birth_year = input("Please enter your four digit birth year: ")
birth_year = int(birth_year)

# This should be changed. We should hard-code the year..
current_year = 2024

# This doesn"t take into account this month. Need to file.
age = current_year - birth_year

print ("You entered: ", birth_year)
print ("Your age is:", age)
