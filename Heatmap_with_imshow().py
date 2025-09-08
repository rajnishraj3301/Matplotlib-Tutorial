import matplotlib.pyplot as plt
matrix = np.random.rand(5, 5)  # Create a 5x5 matrix of random numbers

plt.imshow(matrix, cmap='hot', interpolation='nearest')  # Display matrix as a heatmap
plt.colorbar()  # Add color bar to explain scale
plt.title('Heatmap')  # Title
plt.show()  # Display heatmap
