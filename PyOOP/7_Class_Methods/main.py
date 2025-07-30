class Student:

    # Class variables
    count = 0
    total_gpa = 0

    # Class constructor
    def __init__(self, name, gpa):
        # instance variabless
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    # Class methods
    @classmethod
    def get_count(cls):
        return Student.count

    @classmethod
    def get_total_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

def main():
    student1 = Student("John", 3.2)
    student2 = Student("Jack", 4)

    print(Student.get_count())
    print(Student.get_total_gpa())

if __name__ == "__main__":
    main()