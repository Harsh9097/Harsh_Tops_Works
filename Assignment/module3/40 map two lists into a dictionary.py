# 1). Write a Python program to map two lists into a dictionary.

keys = ['harsh', 'twinkle', 'krish']
values = ['13','18', '15']
number_dictionary = dict(zip(keys, values))
print(number_dictionary)

# This type of  same example for better understanding :

print("\n")
students = ['harsh', 'twinkle', 'vishvam', 'krish']
marks = [89, 95, 92, 86]

students_dict = dict(zip(students, marks))
print(students_dict)