import matplotlib.pyplot as plt  # Importing the pyplot module from matplotlib and aliasing it as plt

x = [1, 2, 3, 4, 5]  # X-axis values
y = [2, 4, 6, 8, 10]  # Y-axis values

plt.plot(x, y)  # Create a line plot with x and y
plt.title('Basic Line Plot')  # Set the title of the plot
plt.xlabel('X-axis')  # Label for X-axis
plt.ylabel('Y-axis')  # Label for Y-axis
plt.grid(True)  # Add a grid to the plot
plt.show()  # Display the plot
