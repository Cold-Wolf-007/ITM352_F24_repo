# Program to test the use pf the HandyMath library.
import HandyMath as HM 

number1 = input("Enter first value:")
number2 = float(input("Enter second value:"))
number1 = float(number1)


mid = HM.midpoint(number1, number2)
print(f"The midpoint is: {mid}" )

squareroot = HM.squareroot(number1)
print(f"The square root of {number1} is {squareroot}")

exp = HM.exponent(number1, number2)
print(f"The value of raising {number1} to the power of {number2} is : {exp} ")

maxsolution =HM.max(number1, number2)
minsolution =HM.min(number1, number2)
print(f"max ,min {maxsolution},{minsolution}")
#print (HM.exponent._name) #last problem