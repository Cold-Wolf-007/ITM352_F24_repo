#ask the user for a year with "leap year" or "not leap year"


year = int(input("What year is it?"))

# if year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")