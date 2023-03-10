
#  1). How Do You Traverse Through A Dictionary Object In Python ?

"""
#  There are multiple ways to iterate over a dictionary in Python :
1.---> Access key using the build .keys()
2.---> Access key without using a key()
3.---> Iterate through all values using .values()
4.---> Iterate through all key, and value pairs using items()
5.---> Access both key and value without using items()
6.---> Print items in Key-Value in pair.
"""
# Example - 1 : Following is an example to iterate through a dictionary using keys() method ?

dictionary = {
   'Novel': 'Pride and Prejudice',
   'year': '1813',
   'author': 'Jane Austen',
   'character': 'Elizabeth Bennet'
}

for keys in dictionary.keys():
    print(keys)


# Example - 2 : Following is an example to iterate through a dictionary using values() method ?

dictionary = {
   'Novel': 'Pride and Prejudice',
   'year': '1813',
   'author': 'Jane Austen',
   'character': 'Elizabeth Bennet'
}
print("\n")
for values in dictionary.values():
   print(values)


# Example - 3 : Iterate through all key, and value pairs using items() ?
print("\n")
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
 
print('List Of given states and their capitals:\n')
 
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)