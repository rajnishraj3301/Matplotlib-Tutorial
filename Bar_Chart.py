import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']  # Categories on X-axis
values = [3, 7, 5, 9]  # Corresponding heights for bars

plt.bar(categories, values)  # Create bar chart
plt.title('Bar Chart')  # Add title
plt.xlabel('Category')  # X-axis label
plt.ylabel('Values')  # Y-axis label
plt.show()  # Display chart
