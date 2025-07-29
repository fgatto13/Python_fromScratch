from abc import ABC, abstractmethod, ABC
from math import pi

class Shape(ABC):
    # We use the abstract method annotation to define an abstract method
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # Every shape has to implement the abstract method
    def area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return pow(self.side, 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base * self.height) * 0.5

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping
    # with the pizza class, we don't need to implement the abstract method.
    # that's because a pizza is a circle, so it is a shape

def main():
    # all the elements in the list are shapes, but in different forms
    shapes = [Circle(4), Square(5), Triangle(2, 3), Pizza(5, "Pepperoni")]
    for shape in shapes:
        # It'll work for pizza too, since a pizza is a circle
        print(f"{shape.area():.2f}")

if __name__ == '__main__':
    main()