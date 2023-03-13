import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Create a circle with radius 5
my_circle = Circle(5)

# Compute the area and perimeter of the circle
circle_area = my_circle.area()
circle_perimeter = my_circle.perimeter()

# Print the area and perimeter of the circle
print("circle area:=",circle_area) 
print("circle perimeter:=",circle_perimeter) 