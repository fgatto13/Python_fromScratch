# Decorators
A **decorator** is a function that *extends* the behavior of another function,
without modifying the base function.

To use them, we pass the base function as an argument to the decorator.
```
@add_sprinkles
get_ice_cream("Vanilla")
```
## ```@property```
Decorator used to define a method as a property, meaning that *it can be accessed like an attribute*
- **benefit**: add additional logic when read, write, or delete attributes
- gives you getter, setter and deleter method

Generally speaking, we use it to improve information hiding inside a class,
by making instance variables **private** (using an underscore _):
```
def __init__(self, attribute1):
    self._attribute1 = attribute1
```
and then using the ``@property`` decorator to define a getter for that attribute.

By doing so, we allow controlled access to the attribute, using getters and setters:
```
# getter
@property
def attribute1(self):
    return f"{self._attribute1}..."
# setter
@attribute1.setter
def attribute1(self, value):
    self._attribute1 = value
```
Getters and setters allow us to create custom behaviors when retrieving information or modifying a value.

There is also the ```@attribute.deleter``` annotation,
which allows us to delete an attribute via a specific method.

The useful part is that, when accessing these methods, you act like you're dealing directly with the attribute:
```
rectangle = Rectangle(100, 100)

print(rectangle.width)

# to access the setter method, we use the assign operator:
rectangle.width = 90

# to access the deleter, we use the del keyword:
del rectangle.width
```