import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4]  # X-axis values
y1 = [i**2 for i in x]  # First line: y = x^2
y2 = [i**3 for i in x]  # Second line: y = x^3

plt.plot(x, y1, label='x^2')  # Plot first line and label it
plt.plot(x, y2, label='x^3')  # Plot second line and label it
plt.title('Multiple Lines')  # Title of the plot
plt.legend()  # Show legend to differentiate lines
plt.show()  # Display plot
