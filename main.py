# Let's consider a basic barplot.
import matplotlib.pyplot as plt
import numpy as np

bars = ('A', 'B', 'C', 'D', 'E')
height = [3, 12, 5, 18, 45]

y_pos = np.arange(len(bars))
plt.bar(y_pos, height)

# If we have long labels, we cannot see it properly
names = ("very long group name 1", "very long group name 2", "very long group name 3", "very long group name 4",
         "very long group name 5")
plt.xticks(y_pos, names, rotation=90)

# Thus we have to give more margin:
plt.subplots_adjust(bottom=0.4)

# It's the same concept if you need more space for your titles
plt.title("This is\na very very\nloooooong\ntitle!")
plt.subplots_adjust(top=0.7)
plt.show()