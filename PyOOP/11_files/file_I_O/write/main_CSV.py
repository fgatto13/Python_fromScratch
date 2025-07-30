# csv (comma separated values)
# files are used to represent a spreadsheet of data
#
# for instance, let's use a 2D data structure:
import csv
# we want to emulate a spreadsheet:
employees = [["Name", "Age", "Job"],
             ["John", 30, "Cook"],
             ["Jack", 42, "Cashier"],
             ["Jones", 22, "Unemployed"]]

file_path = "output.csv"  # we'll keep using relative paths for ease of use

def main():
    try:
        with open(file = file_path, mode = "w") as file:
            writer = csv.writer(file) # writer is an object that allows to interact with csv files
            writer.writerows(employees) # if we use writerows() instead of writerow(), there is no need to iterate
            # for row in employees:
            #     writer.writerow(row)
            print(f"the location '{file_path}' was created")
    except FileExistsError:
        print(f"the location '{file_path}' already exists")
    except:
        print(f"an error occurred")

if __name__ == "__main__":
    main()
