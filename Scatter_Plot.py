import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]  # X values
y = [2, 3, 5, 7, 11]  # Y values

plt.scatter(x, y, color='green', marker='x')  # Create scatter plot with green 'x' markers
plt.title('Scatter Plot')  # Title
plt.xlabel('X values')  # Label X-axis
plt.ylabel('Y values')  # Label Y-axis
plt.grid(True)  # Show grid
plt.show()  # Display plot
