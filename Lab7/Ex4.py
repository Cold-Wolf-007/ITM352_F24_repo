# interate through a list of fares and print out a message indicating
# whether the fare is high or low.

#sample_fares = [8.60, 5.75, 13.25, 21.21]
	
#	for x in sample_fares:
#	    if (x >12):
#	        print(f"This fare {x} is high!")
#	    else:
#	        print(f"This fare {x} is low")


# Function to check if a fare is high or low
def check_fare(fare):
    if fare > 12:
        return f"This fare {fare} is high!"
    else:
        return f"This fare {fare} is low"

# Test cases for check_fare function
def test_check_fare():
    # Test cases
    if check_fare(8.60) != "This fare 8.6 is low":
        print("Test failed for fare 8.60")
    if check_fare(5.75) != "This fare 5.75 is low":
        print("Test failed for fare 5.75")
    if check_fare(13.25) != "This fare 13.25 is high!":
        print("Test failed for fare 13.25")
    if check_fare(21.21) != "This fare 21.21 is high!":
        print("Test failed for fare 21.21")
    else:
        print("All test cases passed!")

# Run the test cases
test_check_fare()
