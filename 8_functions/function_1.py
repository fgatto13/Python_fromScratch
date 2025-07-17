# a function is a block of reusable code, 
# and is declared by putting () after the name of the function to invoke it:
#
# to define a function, use the def keyword, followed by a unique name: def _name ()

def verse():
    print("Happy birthday to you!")

# you can also pass a parameter to a function, but they need to be passed in the correct order
def verse_name(name, age):
    print(f"Happy birthday to {name}! You're {age}")
    
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due: {due_date}")
    
for i in range(1, 4):
    verse()
    verse_name("Fra", 24)
    
display_invoice("Francesco", 42.50, "01/01")