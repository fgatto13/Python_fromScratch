#if is a conditional statement: do something only if a condition is verified
age = int(input("enter your age: " ))

if age >= 21:
    print("you're in")
else:
    print(f"absolutely not! you're only {age}!")

#if a condition is not verified, do something ELSE
#you can add multiple conditions by using ELIF:

age = int(input("enter your age: " ))

if age >= 21 and age < 65:
    print("you're in")
elif age < 0:
    print("you're not even born yet")
elif age >= 65:
    print(f"sorry, {age} is too old")
else:
    print(f"absolutely not! you're only {age}!")
    
online = False
if online:
    print("the user is online")
else:
    print("the user is offline")