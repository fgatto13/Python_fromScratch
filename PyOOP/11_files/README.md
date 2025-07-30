# writing files (.txt, .json, .csv)

when generating a file in a relative path, 
it'll be generated in the same dir as the current file.

We can also use absolute file paths to create a file in a certain location
The open function will return a file object. 
We use "w" specifies that we're opening/creating it in writing mode
The with operator takes care of closing the file for us when we're done
We use as to create an alias
```
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
```
To see all the modes to open a file, check:[GeekForGeeks](https://www.geeksforgeeks.org/python/file-mode-in-python/)