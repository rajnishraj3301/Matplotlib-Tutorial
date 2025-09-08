import matplotlib.pyplot as plt
labels = ['Python', 'Java', 'C++', 'Ruby']  # Pie slice labels
sizes = [40, 30, 20, 10]  # Sizes of each slice

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)  # Create pie chart with labels and percentage
plt.title('Programming Language Popularity')  # Title
plt.axis('equal')  # Make pie a circle instead of oval
plt.show()  # Display chart
