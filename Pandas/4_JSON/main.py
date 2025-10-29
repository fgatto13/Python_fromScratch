import pandas as pd
# to read a json file into a DataFrame, we can use pd.read_json
df = pd.read_json("Pandas/4_JSON/pokedex.json")
print("DataFrame loaded from JSON file:")
print(df.to_string())  # prints the DataFrame