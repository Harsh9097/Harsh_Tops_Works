# 1). Write a Python program to remove an empty tuple(s) from a list of tuples.

list = [(12,30,40),(),(45,60,80),(),('',),("d")]
list = [t for t in list if t]
print(list)


# Here using Define Function :

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 

tuples = [(), ('harsh','13','9'), (), ('vishavam', 'twinkle'),
          ('urvashi', 'moin', '45'), ('',''),()]
print(Remove(tuples))



