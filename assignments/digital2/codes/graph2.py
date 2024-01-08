import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(r):
    return 4 * r * (r + 1)

# Generate a range of values for 'r'
r_values = np.linspace(-10, 10, 100)  # Adjust the range and number of points as needed

# Calculate corresponding 'y' values
y_values = f(r_values)

# Plot the graph
plt.plot(r_values, y_values, label=r'$4 \cdot r \cdot (r+1)$')
plt.title('Graph of $4 \cdot r \cdot (r+1)$')
plt.xlabel('r')
plt.ylabel('$4 \cdot r \cdot (r+1)$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
