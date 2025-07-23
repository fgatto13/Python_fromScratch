from script1 import *

def fav_drink(name):
    print(f"your favorite drink {name}")

def main():
    print("This is the main function")
    fav_drink("manhattan")
    # in this way, we can access a script1 functionality,
    # without needing to execute the whole script
    fav_food("pizza")

if __name__ == "__main__":
    main()