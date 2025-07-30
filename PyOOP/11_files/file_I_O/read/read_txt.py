
def main():
    # file name: input.txt
    file_path = input("Enter the file path: ")
    try:
        with open(file = file_path, mode = "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("the file doesn't exist")
    except PermissionError:
        print("you do not have permission to read this file")

if __name__ == "__main__":
    main()