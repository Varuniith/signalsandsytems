import matplotlib.pyplot as plt
import numpy as np

# Read data from the text file
data = np.loadtxt('points.txt')

# Extract x and y coordinates
x_values = data[:, 0]
y_values = data[:, 1]

# Plot the graph
plt.yticks(np.arange(-3500,4000,500))
plt.stem(x_values, y_values, linefmt='b-',markerfmt='bo',basefmt='r-')
plt.stem(x_values[8], y_values[8], linefmt='g-',markerfmt='go',basefmt='r-')
plt.xlabel('n')
plt.ylabel('a(n)')
plt.grid(True)
plt.savefig('graph.png')
plt.show()
