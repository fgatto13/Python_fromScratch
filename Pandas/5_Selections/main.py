import pandas as pd

df = pd.read_csv('Pandas/5_Selections/data.csv')
print(df)
# to get a list of the headers of the columns
print(df.columns.values.tolist())   # since every name has a space at the beginning:
# Selection by Column
print(df[" Name"].to_string())  # to get the entire column
# without the to_string() method, the data type is a pandas Series
print(type(df[" Name"]))

# we can also select multiple columns at once by passing a list of column names
print(df[[" Name", " Type1"]].to_string())

# Selection by Row
# to select rows, we use the .iloc[] method, since each row has an index
print(df.iloc[1])  # first row
# by using the name of the column, we can select a specific value
df = pd.read_csv('Pandas/5_Selections/data.csv', index_col=" Name") # setting the index to be the Name column
print(df.loc["Pikachu"])  # selecting the row with index "Pikachu"
# we can also pass a Python list of the columns we want to select
print(df.loc["Pikachu", [" Type1", " HP"]])
# we can also select multiple rows using slicing
print(df.loc["Bulbasaur":"Charmander"])  # from Bulbasaur to Charmander (inclusive)
# in the same way, we can use the iloc method to select rows by their integer index
print(df.iloc[0:3])  # first three rows (0, 1, 2)
# you can also get every second row, and specify the first three columns
print(df.iloc[0:11:2, 0:3])  # from row 0 to 10, every second row, and columns 0 to 2