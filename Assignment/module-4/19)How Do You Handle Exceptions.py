"""
19)How Do You Handle Exceptions With Try/Except/Finally In Python?
   Explain with coding snippets. 

===>In Python, you can handle exceptions using a try...except...finally block.  The try block contains the code that might raise an exception, the except blockcontains the code that handles the exception if one is raised, and the finally block contains the code that is always executed, regardless of whether an exception is raised or not.
"""

try:
    # some code that might raise an exception
    x = 10 / 0
except ZeroDivisionError:
    # handle the exception
    print("Cannot divide by zero")
finally:
    # some code that should always be executed
    print("Exiting program")