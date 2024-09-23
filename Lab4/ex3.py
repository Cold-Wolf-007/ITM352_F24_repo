# Manipulate a list in various ways

#list1 = [1,2,3]
#list2 = [4,5,6]
#combined_list = list1 + list2                # C for lists
#print(combined_list)

#string1 = "Hello"
#string2 = "World"
#result = string1 + " " + string2             # c for strings
#print(result)

#result = 5 + 3
#print(result)                               # c for numbers



#responseValues = [5,7,3,8]
# responseValues.append(0)  (((step a)))
# responseValues.insert(2,6) (((step a)))
#responseValues = responseValues + [0]   (((step b)))
#responseValues = responseValues[0:2] + [6] + responseValues[2:] (((step b)))
#responseValues.sort()  # smallest to largest
#responseValues.remove(0)   #first occurance of 0 from the list

#print(responseValues)

# Manipulate a list in various ways



responseValues = [5,7,3,8]
respondentIDs = [1012, 1035, 1021, 1053]

#create a Dictionary with ID values as the keys and survey responses as the values using zip()
surveyDict = dict(zip(respondentIDs, responseValues))
print(surveyDict)