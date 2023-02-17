# How can you pick a random item from a list or tuple ?

"""
# Definition and Usage :
                The choice() method returns a randomly selected element from the specified sequence.
                The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
"""
# Pick random items into List [] :

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))


# Pick random items into Tuple () :
print("\n")

import random

mytuple = (13, 34, "harsh", 9, "python", "dholakiya")

print(random.choice(mytuple))