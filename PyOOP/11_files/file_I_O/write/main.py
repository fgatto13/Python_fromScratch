# writing files (.txt, .json, .csv)

def main():
    txt_data = "I like pizza"

    # when generating a file in a relative path,
    # it'll be generated in the same dir as the current file
    file_path = "output.txt"

    # we can also use absolute file paths to create a file in a certain location

    # The open function will return a file object.
    # We use "w" specifies that we're opening/creating it in writing mode
    #
    # the with operator takes care of closing the file for us when we're done
    #
    # we use as to create an alias
    with open(file = file_path, mode = "w") as file:
        # All the code we write inside here
        # gets executed before closing the file
        file.write(txt_data)
        print(f"txt file {file_path} was created")
    try:
        # we can create a new file by using the x mode,
        # and by inserting everything in this try-except block,
        # we can prevent unexpected behavior if the file already exists
        with open(file = file_path, mode = "x") as file:
            file.write(txt_data)
            print(f"txt file {file_path} was created")
    except FileExistsError:
        print(f"txt file {file_path} already exists")

    # we can also append a file with the 'a' mode
    try:
        with open(file = file_path, mode = "a") as file:
            file.write("\n" + txt_data)
    except Exception:
        print("something went wrong")

    # If we want to add a list of things inside a file:
    employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
    try:
        # remember that the "write" mode overwrites everything inside the file (if it exists)
        with open(file = file_path, mode = "w") as file:
            # we need to iterate the list
            for employee in employees:
                file.write(employee + "\n")
    except FileExistsError:
        print(f"file {file_path} already exists")

if __name__ == "__main__":
    main()