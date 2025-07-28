# an object is an instance of a class,
# that has its own attributes (variables)
# and methods (functions).
#
# a class is the blueprint used to design
# the structure and layout of an object.
#
# a standard class can have as many objects as needed.
class Car:
    # class variables are variables shared among all instances of a class
    wheels = 4

    # the __init__() method is a constructor
    # it initializes the attributes of the class
    # self referes to the object that we're creating
    def __init__(self, model, year, color, for_sale):
        # variables inside the constructor are defined as instance variables,
        # and are specific to the object created
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # we can define methods, or actions that an object can perform
    def drive(self):
        print(f"Driving the {self.color} {self.model}")
    def stop(self):
        print(f"Stopping the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year}, {self.color}, {self.model}, {self.wheels}")