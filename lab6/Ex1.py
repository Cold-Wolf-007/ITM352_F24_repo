# Create a conditional expression that prints if the last element of a tuple is 
# "happy" and the tiple contains more than 3 elements.

emotions = ("sad", "anger", "jealousy", "fear","suprise", "happy")

print((len(emotions) > 3) and (emotions[len(emotions)-1] == "happy"))

if ((len(emotions) >3) and (emotions[len(emotions)-1] == "happy")):
    print("True")
else:
    print("False")