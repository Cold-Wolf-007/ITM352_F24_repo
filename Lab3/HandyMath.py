# Library of Handy reusable math functions
# Given two numbers, returns the numbers between them.

def exponent(num1,num2):
    return (num1**num2)

def max(num1, num2):
    if num1 > num2:
       return(num1)
    else:
       return(num2)
#print(max (20 , 10))
#print(min (10 , 20))    

def min(num1,num2):
   if num1 < num2:
      return(num1)
   else:
      return(num2)


def midpoint(num1, num2):
 return ((num1+num2)/2)

def squareroot(num1):
 return (num1**0.5)
print(squareroot(4))



