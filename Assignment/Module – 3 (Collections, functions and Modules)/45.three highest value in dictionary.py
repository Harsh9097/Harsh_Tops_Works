
# finding 3 highest values in a Dictionary
from heapq import nlargest
 

my_dict = {'A': 67, 'B': 23, 'C': 45,
           'D': 56, 'E': 12, 'F': 69}
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
ThreeHighest = nlargest(3, my_dict, key = my_dict.get)
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for val in ThreeHighest:
    print(val, ":", my_dict.get(val))
