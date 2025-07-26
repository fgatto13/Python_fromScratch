def fav_food(food):
    print(f"your favorite food is {food}")

def main():
    print("This is the main function")
    fav_food("pizza")
    print("Goodbye")

# the reason we use this if statement
# is to tell the program that we want to execute the main code
# only if we're running this script directly
if __name__ == "__main__":
    main()