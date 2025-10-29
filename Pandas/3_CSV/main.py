import pandas as pd
# for the csv data, we'll use a kaggle dataset about the original 151 pokemon
# you can download it from: https://www.kaggle.com/datasets/dizzypanda/gen-1-pokemon

# let's start by reading the CSV file into a DataFrame
df = pd.read_csv("Pandas/3_CSV/data.csv")
print("DataFrame loaded from CSV file:")
# to print all the rows and columns, you can use:
print(df.to_string())  # prints the DataFrame