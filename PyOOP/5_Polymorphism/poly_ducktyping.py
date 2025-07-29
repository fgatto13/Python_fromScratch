class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        animal.speak()
        print(f"Animal is {'alive' if animal.alive else 'dead'}")

if __name__ == "__main__":
    main()