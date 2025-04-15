import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Set the style 
style.use("ggplot")

# Text configs
plt.figure("PIE CHART")
plt.suptitle("PLOT TYPES")
plt.title("PIE CHART")

# Set the values
labels = ("American", "German", "French", "Other")
values = (47, 23, 20, 10)

# Plot the values, add the legends and insert the %
plt.pie(values, labels=labels, autopct="%.2f%%")

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")