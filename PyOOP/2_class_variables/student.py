class Student:
    # this is a class variable
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        # these are instance variables,
        # so distinct values to distinct objects
        self.name = name
        self.age = age
        # to modify a class variable,
        # we use the name of the class instead of self to access it:
        Student.num_students += 1

students = [Student("John", 25), Student("Patrick", 30)]

# you can always access class variables,
# but it is better to use the class name to do so:
print(Student.class_year)

# by doing this, for instance,
# we increment the number of students for each instance created of that class
print(Student.num_students)

print(f"Class of {Student.class_year}: ")
print(f"Number of students: {Student.num_students}")
for stud in students:
    print(print(stud.name, stud.age))