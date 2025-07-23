# strings are an array of characters, commonly used for all sorts of different purposes
# in this file, here are a bunch of examples on how to use different string methods

name = input("enter your full name: ")

# len() gives us the number of characters of the string (including spaces)
result = len(name)
print(result)

# find() returns the position (index) of the first instance of a given character (returns an integer)
result = name.find("F")
print(result)
print(type(result))

# rfind() (reverse find) returns the position (index) of the last instance of a given character (returns an integer)
result = name.rfind("o")
print(result)
# if the function cannot find a single instance, returns -1

# capitalize() capitalizes the first letter of the string, returning a new string:
name = name.capitalize()
print(name)

# upper() makes all the characters inside the string upper case:
name = name.upper()
print(name)

# lower() makes all the characters inside the string lower case:
name = name.lower()
print(name)

# isdigit() returns a boolean to check if the string contains all digits (numbers) (true if yes, false otherwise):
result = name.isdigit()
print(result)

# isalpha() returns a boolean to check if the string contains all alphabetical characters (space is not alphabetical) (true if yes, false otherwise):result = name.isdigit()
result = name.isalpha()
print(result)

number = input("enter your phone number (including dashes '-'): ")
# count() counts the number of instances of a specific character inside a string
counter = number.count("-")
print(counter)

# replace() changes any instance of a certain character with another:
number = number.replace("-", " ")
print(number)

# the help(<type>) command displays all of the commands for a specific type:
print(help(str))