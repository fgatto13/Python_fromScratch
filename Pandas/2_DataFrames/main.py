import pandas as pd
# DataFrame is a two-dimensional labeled data structure, similar to a table in a database or an Excel spreadsheet
# It consists of rows and columns, where each column can have a different data type

# Creating a DataFrame from a dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40]
}

# Create DataFrame
df = pd.DataFrame(data)
print("DataFrame created from dictionary of lists:")
print(df)  # prints the DataFrame

# we're also given a default index (0, 1, 2, 3), but we can set a custom index
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])
print("DataFrame with custom index:")
print(df)  # prints the DataFrame with custom index

# if you need to access specific rows, you can use .loc and .iloc
print("Accessing row for 'Employee 2':")
print(df.loc["Employee 2"])  # access row with label 'Employee 2'
print("Accessing row at position 0:")
print(df.iloc[0])             # access row at position 0

# to add a new column, we'll use a Python list
df["Job Title"] = ["Engineer", "Manager", "Director", "VP"] # each element corresponds to a row, 
# therefore it must match the number of rows
print("DataFrame after adding 'Job Title' column:")
print(df)  # prints the updated DataFrame with new column

# to add a new row, we can create a new DataFrame:
new_row = pd.DataFrame({"Name": ["Eve"], "Age": [28], "Job Title": ["Analyst"]}, index=["Employee 5"])
# then we can use pd.concat to append it to the existing DataFrame
df = pd.concat([df, new_row])   # a depricated method is df.append(new_row)
print("DataFrame after adding new row for 'Employee 5':")
print(df)  # prints the updated DataFrame with new row

# we can also add more than one row at a time
more_rows = pd.DataFrame([{
    "Name": "Frank",
    "Age": 33,
    "Job Title": "Consultant"
}, {
    "Name": "Grace",
    "Age": 29,
    "Job Title": "Intern"
}], index=["Employee 6", "Employee 7"])
df = pd.concat([df, more_rows])
print("DataFrame after adding more rows for 'Employee 6' and 'Employee 7':")
print(df)  # prints the updated DataFrame with more new rows

# let's now output the data on a CSV file
with open("Pandas/2_DataFrames/employees.csv", "w") as file:
    df.to_csv(file)  # save the DataFrame to a CSV file