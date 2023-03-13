"""
15)When will the else part of try-except-else be executed?

===>In a try-except-else block, the else part will be executed only if no exceptions are raised in the try block. 
The purpose of the else block is to provide a way to run some code when no exceptions have been raised, and the try block has executed successfully.
"""

try:
    x=5
    y=0
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    # this code will run only if no exception is raised
    print("The result is:", result)
