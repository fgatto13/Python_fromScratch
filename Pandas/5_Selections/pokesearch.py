import pandas as pd

df = pd.read_csv('Pandas/5_Selections/data.csv', index_col=" Name") # setting the index to be the Name column

# we'll ask the user for the pokemon name
pokemon_name = input("Enter the name of the Pokémon: ")

# we'll try to get the row corresponding to that pokemon name
try:
    # it tries to print the row with that index
    print(df.loc[pokemon_name])
except KeyError:
    # if the pokemon name is not found, it raises a KeyError
    print(f"Pokémon '{pokemon_name}' not found in the dataset.")