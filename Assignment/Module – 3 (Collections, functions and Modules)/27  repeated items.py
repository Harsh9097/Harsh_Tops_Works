# 1).  Write a Python program to find the repeated items of a tuple.

# First type of example :

tuple=(1,3,4,32,1,1,1)  
for i in tuple:
    if tuple.count(i) > 1:
        print("harsh")


# Second type of examaple :
print("\n")
tuple = (13,2,13,4,5,6,7,8,13,1,13)
print(tuple)
count = tuple.count(13)
print(count)