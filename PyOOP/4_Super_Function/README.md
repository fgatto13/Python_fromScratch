super() is a function used in a child class to call methods from a parent class (Super class).
```
class Shape:
    def __init__(self, attribute):
        self.attribute = attribute
class Circle(Shape):
    def __init__(self, attribute1, attribute2):
        super().__init__(attribute1)
        self.attribute2 = attribute2
```

It allows you to extend the functionality of the inherited methods

We can also override methods defined in the super class
```
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f'{self.color} is {'filled' if self.filled else 'not filled'}.')
class Circle(Shape):
    def __init__(self, radius, color, filled):
        super().__init__(color, filled)
        self.radius = radius
    @override
    def describe(self):
        super().describe()
        print(f'{self.color} is {self.radius} cm.')
```