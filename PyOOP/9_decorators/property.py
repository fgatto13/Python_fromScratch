class Rectangle:
    def __init__(self, width, height):
        # we can make attributes private (which is a best practice) using an underscore:
        self._width = width
        self._height = height
    # by using the property decorator, we can create custom getters:
    @property
    def width(self):
        return f"{self._width}cm"
    @property
    def height(self):
        return f"{self._height}cm"
    # we can then use the attribute's name to create a setter:
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("width must be positive")
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("height must be positive")
    # we can also create a deleter for a specific attribute:
    @width.deleter
    def width(self):
        del self._width
        print("width deleted")
    @height.deleter
    def height(self):
        del self._height
        print("height deleted")



def main():
    rectangle = Rectangle(100, 100)
    print(rectangle.width)
    # to access the setter method, we use the assign operator:
    rectangle.width = 90
    # to access the deleter, we use the del keyword:
    del rectangle.width

if __name__ == "__main__":
    main()