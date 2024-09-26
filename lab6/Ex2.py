#myList = [
#[1,2, "abc", (1,2,3), True, ["a",2,3],10,20,33, "howdy", False],
#[1,2, "abc", (1,2,3)],
#[1,2, "abc", (1,2,3),True]
#]
#if (len(myList[2]) < 5):
 #   print("Less than 5 elements")
#elif(5 <= len(myList[2]) <= 10):
 #   print("Between 5 and 10 elements")
#else:
 #   print("Greater than 11 elements ")

# Function to check and print the message based on list length
def check_list_length(lst):
    length = len(lst)
    if length < 5:
        return "Less than 5 elements"
    elif 5 <= length <= 10:
        return "Between 5 and 10 elements"
    else:
        return "More than 10 elements"

# Test cases with different lengths
test_cases = [
    [],  # Empty list
    [1, 2],  # Fewer than 5 elements
    [1, 2, 3, 4, 5],  # Exactly 5 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9],  # 9 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Exactly 10 elements
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # More than 10 elements
]

# Loop through the test cases and apply the function
for test_case in test_cases:
    print(f"List {test_case} -> {check_list_length(test_case)}")