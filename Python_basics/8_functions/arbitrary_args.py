# arbitrary meaning a varying amount of arguments:
#   *args       = allows you to pass multiple non-key arguments
#   **kwargs    = allows you to pass multiple keyword arguments
#               * is called unpacking operator
#   *args corresponds to a tuple of arguments
#   **kwargs corresponds to a dictionary of {keyword: value} pairs

def add(*nums):
    total = 0
    for x in nums:
        total += x
    return total

print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
        
display_name("Giorgio", "Giacomo", "Giovanni")

# let's now see some examples for kwargs:
def print_address(**kwargs):
    # being a dictionary, you can use its methods:
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake str.", city="Detroit", state="MI", zip="81031")

# you can also use args and kwargs together:
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for kwrd in kwargs.values():
        print(kwrd, end=" ")
    print()
    # you can also use the get method:
    if "apt" in kwargs: # that allows us to check wether a key is present or not
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# *args must go before **kwargs, otherwise it's going to return a synthax error
shipping_label("Dr.", 
               "Spongebob", 
               "Squarepants",
               street="123 Fake str.", 
               city="Detroit", 
               state="MI", 
               zip="81031")