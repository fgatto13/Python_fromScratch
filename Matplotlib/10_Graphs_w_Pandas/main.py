import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Matplotlib/10_Graphs_w_Pandas/data.csv")

td_drivers = df[df["Decade"] >= 2020]
print(td_drivers)
# let's focus on drivers' nationality
n_count = td_drivers["Nationality"].value_counts()    # returns the number for each category (as a Series)

# we want to plot the index (nation) and value
plt.barh(n_count.index, n_count.values)

plt.xticks(n_count)
plt.title("# of drivers in modern F1 per nationality")
plt.xlabel("Count")
plt.ylabel("Nationality")

plt.tight_layout()
plt.show()