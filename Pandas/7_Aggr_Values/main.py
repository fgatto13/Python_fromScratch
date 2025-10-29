import pandas as pd
# Aggregate functions: reduces a set of values into
# a single summary value (e.g., sum, mean, count, etc.)
# Used with groupby to summarize data (groupby())

df = pd.read_csv("Pandas/7_Aggr_Values/data.csv")
# we can, for instance, compute the mean of all numeric columns
print(df.mean(numeric_only=True))  # Mean of numeric columns

# we can sum all numeric columns
print(df.sum(numeric_only=True))  # Sum of numeric columns

# we can find the minumum value in all numeric columns
print(df.min(numeric_only=True))  # Minimum of numeric columns

# we can find the maximum value in all numeric columns
print(df.max(numeric_only=True))  # Maximum of numeric columns

# we can count the number of non-null values in all columns (doesn't need kwarg)
print(df.count())  # Count of non-null values in all columns

# these aggregate functions do apply for all the dataframe
# but we can use the subscript operator to select specific columns
print("--- Championships mean ---")
print(df["Championships"].mean(numeric_only=True))
print("--- Fastest_Laps sum ---")
print(df["Fastest_Laps"].sum(numeric_only=True))
print("--- Years_Active min ---")
print(df["Years_Active"].min(numeric_only=True))
print("--- Race_Wins max ---")
print(df["Race_Wins"].max(numeric_only=True))
print("--- Seasons count ---")
print(df["Seasons"].count())

# we can also use groupby to group the data by a specific column
# and then apply aggregate functions to each group
grouped = df.groupby("Nationality") # we create a group object, and we'll group by Nationality
# so if you print grouped you get a DataFrameGroupBy object
# we can apply aggregate functions to each group
print("--- Wins by Nationality ---")
print(grouped["Race_Wins"].sum(numeric_only=True))  # Sum
print("---  Count by Nationality ---")
print(grouped["Nationality"].count())  # Count