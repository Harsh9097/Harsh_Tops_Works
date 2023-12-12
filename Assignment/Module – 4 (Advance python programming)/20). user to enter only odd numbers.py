"""
20)Write python program that user to enter only odd numbers, else will
raise an exception
"""

try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError("Even number entered")
    else:
        print("Odd number entered")
except ValueError as ve:
    print(ve)