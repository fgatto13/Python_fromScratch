import pandas as pd

# filtering: keeping the rows that match a condition
df = pd.read_csv("Pandas/6_Filtering/data.csv")
# we'll want to keep only the champions in F1 history
champions = df[df["Champion"] == True]
print(champions)

# now let's filter by nationality
italian_drivers = df[df["Nationality"] == "Italy"]
print(italian_drivers)

# or by number of championships won
multiple_champions = df[df["Championships"] > 0.0]
print(multiple_champions)

# now let's use logical operators
# drivers who are italian and have won championships
italian_multiple_champions = df[
    (df["Nationality"] == "Germany") & 
    (df["Championships"] > 0.0)
]
print(italian_multiple_champions)

# drivers who have won more than one race or have more than 1 podium
successful_drivers = df[
    (df["Race_Wins"] > 1) |
    (df["Podiums"] > 1)
]
print(successful_drivers)