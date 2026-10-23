import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*self.radius**2
    

circle1 = Circle(5)
print(f"The area of the circle is: {circle1.get_area()}")

circle2 = Circle(2)
print(f"The area of the circle is: {circle2.get_area()}")
