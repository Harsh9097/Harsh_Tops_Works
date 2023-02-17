# 1). Write a Python program to replace last value of tuples in a list.

l1 = [("vishvam","twinkle","krish"), ("urvashi","kaushal","moin"), ("aman","rakesh","anjali")]
print(l1)

print([t[:-1] + ("harsh",) for t in l1])