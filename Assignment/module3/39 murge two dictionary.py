# 1). Write a Python script to merge two Python dictionaries.

# Example 1 : Using copy() and update()

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)

print(d)

# Example 2 : Using the | Operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)