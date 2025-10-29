import matplotlib.pyplot as plt
import numpy as np

# Histograms are used to represent the distribution of quantitative data.
# Values are grouped into intervals and it counts how many fall in each range.

scores = np.random.normal(
    loc=80,     # location of the center of generated data (basically the most frequent value)
    scale=10,   # standard deviation (or spread). higher means greater deviation 
    size=100
)
scores = np.clip(scores, 0, 100)    # every score below 0 goes to 0, same for scores above 100

plt.hist(
    scores, 
    bins=10,    # bins = intervals
    color="lightgreen",
    edgecolor="black"
)

plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("# of Students")

plt.show()