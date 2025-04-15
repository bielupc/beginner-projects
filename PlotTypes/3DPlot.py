import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Text configs
plt.figure("3D PLOT")
plt.suptitle("3D PLOT")

# Create the 3D environment 
ax = plt.axes(projection="3d")

# Set X/Y/Z values
z = np.linspace(0, 20, 100)
x = np.sin(z)
y = np.cos(z)

# Plot the values
ax.plot3D(x,y,z)

# Show the plot
plt.show()

# Save the plot with plt.savefig("line_plot.png")