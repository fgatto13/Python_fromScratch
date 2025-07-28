# inheritance is an OOP mechanism
# that allows a child class to inherit its super class
# characteristics (variables and methods),
# while also adding new features.
#
# for instance, a student is a person,
# therefore, person is a super class of student.
#
# when the student class inherits the person's class,
# it inherits attributes such as name and age,
# plus adding new features such as grade average and so on
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# to inherit a class,
# we use the Sub(Super): structure
class Student(Person):
    def __init__(self, name, age, mode):
        # we always need to call the super constructor
        super().__init__(name, age)
        self.mode = mode

# it helps with reusability and extensibility