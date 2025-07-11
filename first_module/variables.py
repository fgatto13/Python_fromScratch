#variables: container for a value (string, integer, float, boolean)

#Strings: series of characters
first_name = "Fra"
#you can print variables with the print statement
print(first_name)
#and also insert them inside other strings, by using a formatted string (f"{}"):
print(f"Hello {first_name}")

#integers: whole numbers
age = 25
print(age)
print(f"you are {age} years old")

#floats: floating points
price = 25.6
print(f"price is {price}")

#booleans: true or false
is_student = True
print(f"student? {is_student}")
#they're more used as internal variables, not really used as display variables:
if is_student:
    print("yes")
else:
    print("no")