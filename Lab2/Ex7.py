# Ask the user to input a temperature in degrees Fahrenheit
# Convert the temperature to Celslus and output it.

degreesF = input("Enter a temperature in Fahrenheit: ")

degreesC = (float(degreesF)-32) * (5/9) 

print ("This converts to ", degreesC, "Celsius")
