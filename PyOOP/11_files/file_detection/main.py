# File detection

import os

def main():
    # for file detection, we can use both relative and absolute paths
    # 1. relative:
    file_path = "test.txt"
    # the relative file path checks in the same directory as the current file
    path2 = "files/test.txt"

    # the path.exists(file) function returns a boolean value and checks wether a file in the path exists or not
    if os.path.exists(file_path):
        print(f"the location '{file_path}' exists")
    else:
        print("that location does not exist")

    if os.path.exists(path2):
        print(f"the location '{path2}' exists")
    else:
        print("that location does not exist")

    # 2. absolute path:
    abs_file_path_1 = "/Users/francescogatto/Documents/personale/Python_fromScratc/PyOOP/11_files/file_detection/test.txt"
    if os.path.exists(abs_file_path_1):
        print(f"the location '{abs_file_path_1}' exists")
         # the path.isfile(file_name) function checks if the parsed element is actually a file and not a directory:
        if os.path.isfile(abs_file_path_1):
            print(f"the location '{abs_file_path_1}' is a file")
        # the path.isdir(name) function checks if a name is a directory
        elif os.path.isdir(abs_file_path_1):
            print(f"the location '{abs_file_path_1}' is a directory")
    else:
        print("that location does not exist")


if __name__ == "__main__":
    main()