# 1). How Do You Check The Presence Of A Key In A Dictionary ? 


"""
 # Check If Key Exists using the Inbuilt method keys() :
    Using the Inbuilt method keys() method returns a list of all the available keys in the dictionary. 
        With the Inbuilt method keys(), use if statement with ‘in’ operator to check if the key is present in the dictionary or not. 
# There can be different ways for checking if the key already exists, we have covered the following approaches :
1). -----> Using the Inbuilt method keys() 
2). -----> Using if and in
3). -----> Using has_key() method
4). -----> Using get() method
Defination : Using has_key() method returns true if a given key is available in the dictionary, otherwise, 
                    it returns a false. With the Inbuilt method has_key(), 
                            use the if statement to check if the key is present in the dictionary or not.
"""

# Example of check our key is presence in dictionary :

my_dict = {1: 'a', 2: 'b', 3: 'c'}

if 2 in my_dict:
    print("Key is present")
else:
    print("Not Present")