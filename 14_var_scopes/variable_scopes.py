# the scope of a variable is where a variable is visible and accessible
# the scope resolution is enclosed in (LEGB), meaning:
#   1.  Local
#   2.  Enclosed
#   3.  Global
#   4.  Built-in
# When resolving the scope of a variable, it does so by following the order:
#   Local -> Enclosed -> Global -> Built-in

# a local variable is a variable defined inside a function, 
# and therefore not visible nor accessible outside the function:
def funct():
    x = 1       # x is a local variable
    print(x)

# the enclosed scope is used when we define a function inside another function
def funct1():
    x = 1   # this is an enclosed variable, meaning that it can be accessed in an inner function, but not in an outer function
    def funct2():
        print(x)
    funct2()

# a global variable is a variable visible in the entire module:
x = 3   # this variable can be accessed by all of the other functions and expressions

# lastly, a built-in variable is a variable accessible from another module, such as pi in math