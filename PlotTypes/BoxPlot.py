import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Text configs
plt.figure("BOX PLOT")
plt.suptitle("PLOT TYPES")
plt.title("BOX PLOT")
plt.ylabel("Y VALUES")


# Set the values
mu, sigma = 172, 4
y_values = np.random.normal(mu, sigma, 200)

# Plot the values
plt.boxplot(y_values)

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")