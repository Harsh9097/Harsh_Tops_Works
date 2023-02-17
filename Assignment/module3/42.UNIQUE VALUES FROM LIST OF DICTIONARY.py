# 1). Write a Python program to print all unique values in a dictionary.


# METHOD OF UNIQUE VALUES FROM LIST OF DICTIONARY : 
"""
Using set() + values() + dictionary comprehension The combination of these methods can together help us achieve the task of getting the unique values. 
    The values function helps us get the values of dictionary, 
 set helps us to get the unique of them, and dictionary comprehension to iterate through the list.
"""



# Get Unique values from list of dictionary.
# Using set() + values() + dictionary comprehension.

list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",list)

u_value = set( val for dict in list for val in dict.values())
print("Unique Values: ",u_value)

print(len(u_value))