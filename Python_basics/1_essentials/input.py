#input() = function that prompts the user to enter data
isTrue = False
while isTrue == False:
    if isTrue:
        print(f"Hello {name}!")
    else:
        name = input("insert name: ")
        print(f"inserted name: {name}")
        isTrue = bool(input("is it right? insert any key if so, or enter if not: "))
age = int(input("now insert age: "))
print(f"your age is: {age}")
print(f"next year, you're gonna be {age + 1}")

