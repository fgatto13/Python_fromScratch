from typing_extensions import override

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f'{self.color} is {'filled' if self.filled else 'not filled'}.')

class Circle(Shape):
    def __init__(self, radius, color, filled):
        # we use the super method to call the constructor of the super class
        super().__init__(color, filled)
        self.radius = radius
    # we can also override a method from the super class
    @override
    def describe(self):
        super().describe()
        print(f'{self.color} is {self.radius} cm.')

class Square(Shape):
    def __init__(self, width, color, filled):
        super().__init__(color, filled)
        self.width = width
    @override
    def describe(self):
        super().describe()
        print(f'{self.color} is {self.width} cm.')

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
    @override
    def describe(self):
        super().describe()
        print(f'{self.color} is {self.width} cm and {self.height} cm.')

def main():
    triangle = Triangle(color='red', filled=True, width=10, height=1)
    print(triangle)
    square = Square(width=2, color='blue', filled=True)
    print(square)
    circle = Circle(radius=2, color='green', filled=True)
    print(circle)
    circle.describe()
    triangle.describe()
    square.describe()

if __name__ == '__main__':
    main()