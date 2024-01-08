import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(n):
    return (-1)**(n-1) * n**3

# Generate a range of values for 'n'
n_values = np.arange(1, 14, 1)  # Adjust the range as needed

# Calculate corresponding 'y' values
y_values = [f(n) for n in n_values]

# Plot the graph
plt.plot(n_values, y_values, marker='o', linestyle='-')
plt.title(r'Graph of $(-1)^{n-1} \cdot n^3$')
plt.xlabel('n')
plt.ylabel(r'$(-1)^{n-1} \cdot n^3$')
plt.grid(True)
plt.show()