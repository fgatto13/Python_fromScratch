# return is a keyword that is used to end a function by sending a result back to the caller

def add(x, y): 
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y): 
    return x * y

def divide(x, y): 
    return x / y

def create_name(first, last):
    return first.capitalize() + " " + last.capitalize()
    

print(add(5, 4))
print(subtract(5, 4))
print(multiply(5, 4))
print(divide(5, 4))
print(create_name("spongebob", "squarepants"))

# these are called positional arguments