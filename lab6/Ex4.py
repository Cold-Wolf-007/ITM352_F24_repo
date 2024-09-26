# ask the users age and if its tuesday/matinee
age = int(input("Please enter your age: "))
is_tuesday = input("Is it a Tuesday? (yes/no): ").lower() == 'yes'
is_matinee = input("Is it a matinee show? (yes/no): ").lower() == 'yes'

# Normal price
normal_price = 14

#conditions
if is_matinee:

 if age>= 65:
  price = 5
 else:
  price = 8
elif age >= 65:
  price=10
print(f"Age: {age}, Tuesday: {is_tuesday}, Matinee: {is_matinee}")
print(f"Movie price: ${price}")