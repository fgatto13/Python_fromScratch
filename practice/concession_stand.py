# In this program, we're gonna use a dictionary to store {item: price} pairs
#   so, the output is going to be a simple menu

menu = {"pizza": 3.95,
        "hot-dog": 5.00,
        "cola": 2.50,
        "popcorn": 3.95}

total = 0
cart = []

for key, value in menu.items():
    print(f"{key:10}{value:>10,.2f}$")

while True:    
    key = input("Select an item from the menu: ").lower()
    value = menu.get(key)
    if value:
        print(f"You selected {key}, your price is going to be: {value}")
        total += value
        cart.append(key)
    else:
        print(f"Sorry, {key} is not in the menu")
    answer = input("Would you like anything else? Y/N: ").upper()
    if answer == "N":
        break
    
print("You selected the following items: ")
for item in cart:
    print(item)
print(f"Your total is going to be: {total:.2f}$")