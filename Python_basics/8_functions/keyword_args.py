# a keyword argument is an argument preceded by an identifier.
#   it helps with readability
#   order doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
    
# to use a keyword argument, we assign the value to the parameter explicitly:
hello(greeting="hello", title="Mr.", first="Spongebob", last="Squarepants")
# remember that positional arguments come always first!:
hello("Hello", title="", first="", last="")

# for instance, the print() function uses end="" as a keyword argument:
for x in range(1, 11):
    print(x, end=" ")
print()
# it also uses sep="" as separate:
print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=39, area=132, first=456, last=7890)
print(phone_num)