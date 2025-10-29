import pandas as pd
# Data Cleaning: process of fixing or removing
# incomplete, incorrect, or irrelevant data.
# This is the main use of Pandas library.

df = pd.read_csv("Pandas/8_Data_Cleaning/data.csv")
# 1. Drop irrelevant columns
df = df.drop(columns=["Podium_Rate", "Start_Rate"])
print(df)

# 2. Handle missing data
# Option A: Drop rows with any missing values
df = df.dropna(subset=["Championship Years"])   # drop rows where 'Championship Years' is NaN
print(df.to_string())
# Option B: Fill missing values with a specific value
df = df.fillna({"Champion": 0})  # fill NaN with 0
print(df.to_string())

# 3. Correct any inconsistent values
df["Nationality"] = df["Nationality"].replace(
    {"Italy":"ITA",
     "Germany":"GER"}) # The replace function returns a Series, and takes as parameter a dictionary: key being the old value, value being the new value
print(df.to_string())

# 4. Standardize Text
df["Driver"] = df["Driver"].str.lower()  # convert all text in 'Driver' column to lowercase

# 5. Fix or change data types
df["Champion"] = df["Champion"].astype(int)  # convert 'Champion' column to integer type
print(df.to_string())

# 6. Remove duplicates
df = df.drop_duplicates()  # remove duplicate rows
print(df.to_string())