# Examine every element
# Within the loop, use an if statement to count how many of the 
# elements are strings, After the lloop completes, print out a message
# Stating how many strings are in the tuple

weird = ("hello", 10, "goodbye", 2, "goodnight", 5)
numStrings = 0

for x in weird:
    if (type(x) is str):
        numStrings += 1

print(f"We have {numStrings}strings")