"""
23) Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

my_rectangle = Rectangle(5, 10)

# Compute the area of the rectangle
rectangle_area = my_rectangle.area()

# Print the area of the rectangle
print(rectangle_area)  # Output: 50