import numpy as np  # Import numpy for generating data
import matplotlib.pyplot as plt
data = np.random.randn(1000)  # Generate 1000 random numbers (normal distribution)

plt.hist(data, bins=30, color='purple', edgecolor='black')  # Create histogram with 30 bins
plt.title('Histogram of Random Data')  # Title
plt.xlabel('Value')  # X-axis label
plt.ylabel('Frequency')  # Y-axis label
plt.show()  # Show plot
