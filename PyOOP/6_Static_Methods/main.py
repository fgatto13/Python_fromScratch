class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    # get_info() is an instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    # to create a static method, we'll use the staticmethod decorator
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

def main():
    employee1 = Employee("James", "Manager")
    employee2 = Employee("John", "Cashier")
    employee3 = Employee("Jack", "Cook")

    # To use a static method, we use the name of the class:
    print(Employee.is_valid_position("Manager"))

    # With an instance method, you use the instance of a class:
    print(employee1.get_info())
    print(employee2.get_info())
    print(employee3.get_info())

if __name__ == "__main__":
    main()