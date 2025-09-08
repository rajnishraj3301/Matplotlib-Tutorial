import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']  # Y-axis categories
values = [3, 7, 5, 9]  # Bar lengths

plt.barh(categories, values, color='skyblue')  # Horizontal bars with custom color
plt.title('Horizontal Bar Chart')  # Chart title
plt.xlabel('Values')  # X-axis label
plt.ylabel('Category')  # Y-axis label
plt.show()  # Show plot
