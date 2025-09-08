import matplotlib.pyplot as plt  
x = [0, 1, 2, 3, 4]  # X-axis values
y = [0, 1, 4, 9, 16]  # Y-axis values (squares)

plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o')  # Customize line color, width, style, and markers
plt.title('Customized Line Plot')  # Set title
plt.xlabel('X')  # Label X-axis
plt.ylabel('Y = X^2')  # Label Y-axis
plt.show()  # Show the plot
