# How can you pick a random item from a range ?


# The following program returns a random numbers within the given range using random.randrange() function −

import random
x = random.randrange(1,50)
print(x)


# getting an alternative (odd number) random number from 1 to 50 :

print("\n")
y = random.randrange(1,50,2) # Here using print for Odd Number.......
print(y)

# getting an alternative (even number) random number from 1 to 50 :

print("\n")
z = random.randrange(2,50,2) # Here using print for Even Number........
print(z)