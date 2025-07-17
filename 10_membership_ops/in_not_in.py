# Membership operators are used to test wether a value or a variable is found in a sequence:
#   1. in
#   2. not in
# can be used in all sorts of collections (strings, lists, tuple, set and dictionary)
# Basically, it performs a search,
# without you needing to implement any specific algorithm to search inside a sequence

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

# in returns True if found, False otherwise
if letter in word:
    print(f"{letter} was found")
else:
    print(f"{letter} was not found")
    
# not in returns True if not found, False otherwise
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"{letter} was found")
    
# the behavior is similar for lists, tuples and sets
students = {"Spongebob", "Patrick", "Sandy"}

stud = input("Insert the name: ")

if stud in students:
    print(f"{stud} is a student")
else:
    print(f"{stud} was not found")

if stud not in students:
    print(f"{stud} was not found")
else:
    print(f"{stud} is a student")
    
# for dictionaries:
grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick": "D"}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}") # we use the student as our index
else:
    print(f"{student} was not found")
    
email = "MarioRossi123@example.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")