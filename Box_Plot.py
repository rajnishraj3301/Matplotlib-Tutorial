import matplotlib.pyplot as plt
data = [np.random.normal(0, std, 100) for std in range(1, 4)]  # Create 3 groups of normally distributed data

plt.boxplot(data)  # Create box plot
plt.title('Box Plot Example')  # Title
plt.xlabel('Group')  # Label X-axis
plt.ylabel('Values')  # Label Y-axis
plt.show()  # Show plot
