class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("Squeek!")

dog = Dog("Barney")
cat = Cat("Jack")
mouse = Mouse("Bobby")
# you can use the super class methods:
dog.eat()
cat.eat()
mouse.eat()

dog.sleep()
cat.sleep()
mouse.sleep()

# and access the names (instance variable defined in Animal)
print(dog.name)
print(cat.name)
print(mouse.name)