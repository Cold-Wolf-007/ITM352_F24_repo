# Loop through number from 1 to 10
for num in range(1,11):
    if num == 5:
        continue # skip if 5
    if num == 8:
        print("Reached 8, stopping the loop.")
        break # Stop when loop gets to 8
    print(num)