# a while loop executes some code while a condition is verified

name = input("enter your name: ")

while name == "":
    print("name not inserted")
    name = input("enter your name: ")

#you can combine logical operators inside the while condition:

age = int(input("enter your age: "))

while age < 0 or age > 120:
    print("age must be between 0 and 120")
    age = int(input("enter your age: "))
print(f"hello, {name}! You're {age} years old")

food = input("enter a food you like: ")
while not food == "q":
    print(f"{name}, you like {food}!")
    food = input("enter another food you like (or q to exit): ").lower()
print("byebye")