# to create a decorator, we create a decorator function:
# we pass the function as a parameter
def add_sprinkles(func):
    # then, we define a nested wrapper function
    def wrapper(*args, **kwargs):
        # in which we call the parsed function,
        # with the custom behavior added
        print("adding sprinkles🎊")
        func(*args, **kwargs)
    # and lastly, we return the wrapper function
    return wrapper

# it is necessary to add the wrapper because,
# by doing that, the custom behavior gets called
# only when the decorated function gets called

# we can create and apply multiple decorators
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("adding fudge🍫")
        func(*args, **kwargs)
    return wrapper
# By adding *args and **kwargs to the decorator function,
# we can manage all the args parsed to the decorated function

# to add a decorator to a function,
# we use the annotation @ followed by the custom name (similar to Java)
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice Cream🍦")

get_ice_cream("Vanilla")