import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 250, 275, 225])
colors = ["red", "green", "blue", "yellow"]

# to create a pie chart, we'll use the pie() function
plt.pie(
    values, 
    labels=categories,
    autopct="%1.1f%%",
    colors=colors,
    explode=[0,0,0,0.1],
    shadow=True,
    startangle=90
)
plt.title("Sample Title")
plt.show()