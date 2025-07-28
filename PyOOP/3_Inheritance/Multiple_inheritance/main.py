# the animal class is a grandparent
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

# Prey and Predator are two parent classes
class Prey(Animal):
    def flee(self):
        print(f"this {self.name} is fleeing...")

class Predator(Animal):
    def hunt(self):
        print(f"this {self.name} is hunting...")

# A rabbit is only a Prey, so it inherits from just that class
class Rabbit(Prey):
    pass

# A hawk is only a predator, so it inherits from just that class
class Hawk(Predator):
    pass

# a fish hunts smaller fishes, but flees from bigger fishes, so it inherits both classes
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Hawk")
fish = Fish("Nemo")
# all three animals are gonna be able to use the methods inherited by the animal class
rabbit.eat()
hawk.eat()
fish.eat()
rabbit.sleep()
hawk.sleep()
fish.sleep()
# fish can access methods from both predator and prey classes:
fish.hunt()
fish.flee()

# this example covers both multiple and multi-level inheritance