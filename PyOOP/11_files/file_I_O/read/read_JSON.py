import json

def main():
    # file name: input.json
    file_path = input("Enter the file path: ")
    try:
        with open(file = file_path, mode = "r") as file:
            content = json.load(file)   # we use the json.load(file) method to read from a json file
            # the content will be a dictionary
            print(content)
    except FileNotFoundError:
        print("the file doesn't exist")
    except PermissionError:
        print("you do not have permission to read this file")

if __name__ == "__main__":
    main()