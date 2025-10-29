import matplotlib.pyplot as plt
import numpy as np

# bar charts compare different categories of data using rectangular bars.
categories = np.array(["Grains", "Fruits", "Vegetables", "Dairy", "Meat"])
values = np.array([25, 15, 30, 10, 20])

plt.title("Consumption by the day")
plt.xlabel("Food")
plt.ylabel("Quantities")
# to create a bar chart, we'll use the bar method
plt.bar(categories, values) # barh creates an horizontal one
plt.show()