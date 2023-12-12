# 1). Write a Python program to calculate the area of a trapezoid ?

"""
FORMULA OF TRAPEZOID :
            Area = 1\2 (a + b) * height
"""

height = float(input("Height of trapezoid: "))

base_1 = float(input('Base one value: '))
base_2 = float(input('Base two value: '))

area = ((base_1 + base_2) / 2) * height
median = ((base_1 + base_2) / 2)

print("Area of Trapezoid : ", area)
print("Median of Trapezoid : ", median)