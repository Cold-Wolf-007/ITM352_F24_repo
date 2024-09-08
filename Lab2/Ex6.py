# Ask the user to enter their weight in pounds. Convert to kilos and output

weight_in_pounds = input("please enter your weight in pounds: ")

weight_in_pounds = float(weight_in_pounds)
KILOS_PER_POUND =0.453592
 
weight_in_kilos = weight_in_pounds * KILOS_PER_POUND

print(weight_in_pounds, "pounds is", weight_in_kilos, "kilograms")
