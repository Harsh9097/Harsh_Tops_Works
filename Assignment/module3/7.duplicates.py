""""
7) Write a Python program to remove duplicates from a list. 
"""


l1 = [12,34,56,78,34]


l1 = set(l1)
l1.remove(34)
l1 = list(l1)

print(l1)

# Second types of Duplicate elements remove.

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(set(duplicate))