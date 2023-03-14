# 1). Write a Python program to combine two dictionary adding values for common keys. 

from collections import Counter

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
new_dict = Counter(dict1) + Counter(dict2)

print("The new_dict is : ",new_dict)



# Example : 2 - Using Looping method for combine adding two dictionary values for common keys.

print("\n")

dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'harsh': 100, 'rami': 200, 'for': 300}

for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
         
print(dict2)