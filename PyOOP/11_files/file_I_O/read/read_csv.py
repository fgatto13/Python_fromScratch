import csv

def main():
    # file name: input.csv
    file_path = input("Enter the file path: ")
    try:
        with open(file = file_path, mode = "r") as file:
            content = csv.reader(file) # we will use the reader method to read a csv file
            for line in content:
                print(line)
                # being a list of lists, you can use the index operator to print a single column (or row)
                # print(line[0])
    except FileNotFoundError:
        print("the file doesn't exist")
    except PermissionError:
        print("you do not have permission to read this file")

if __name__ == "__main__":
    main()