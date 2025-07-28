from car import Car

def main():
    # to create an object, we call the constructor and parse the parameters:
    car1 = Car('A1', 2022, color = 'blue', for_sale = True)
    # we can create as many objects as we want
    car2 = Car('A3', 2024, color = 'red', for_sale = True)
    car3 = Car('A4', 2024, color = 'green', for_sale = True)
    # if we print the object itself, we get the memory address in which it is stored
    # we can print specific attributes:
    print(car1.model)
    print(car1.year)
    print(car1.color)
    print(car1.for_sale)

    # and access methods:
    car1.drive()
    car1.stop()
    car1.describe()

if __name__ == "__main__":
    main()