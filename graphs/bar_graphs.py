import matplotlib.pyplot as plt
import numpy as np
import random

# Function to generate a list of distinct colors in HSV color space
def generate_colors(num_colors):
    colors = []
    for i in np.linspace(.4, .7, num_colors):
        hue = i
        saturation = 0.9  # Adjust as needed
        value = 0.9       # Adjust as needed
        rgb_color = plt.cm.hsv(hue)
        colors.append(rgb_color[:3])
    return colors

# Fake data
people = ['Joe', 'Alice', 'John']
methods = ['In Person', 'Email', 'Carrier Pigeon', 'Mailbox', 'FedEx', 'UPS', 'DHL']

# Generate random data for the number of mails received from each person and method
num_methods = len(methods)
num_people = len(people)
data = np.random.randint(1, 10, size=(num_people, num_methods))

# Define the number of distinct colors needed
num_colors = len(methods)

# Generate a list of distinct colors
custom_colors = generate_colors(num_colors)

data = np.array([
    [3, 4, 1, 2, 5, 6, 2],  # Joe's mail count for each method
    [2, 3, 4, 1, 3, 2, 5],  # Alice's mail count for each method
    [4, 2, 1, 3, 2, 4, 1]   # John's mail count for each method
])


# Create a stacked bar graph
fig, ax = plt.subplots()

# Shuffle the custom colors randomly to match the methods
random.shuffle(custom_colors)

# Create bars for each method using the custom color palette
for i, method in enumerate(methods):
    ax.bar(people, data[:, i], label=method, color=custom_colors[i], alpha=0.7, bottom=np.sum(data[:, :i], axis=1))

# Add labels and a legend
ax.set_xlabel('People')
ax.set_ylabel('Number of Mails')
ax.set_title('Mail Received by Bob')
ax.legend(title='Mail Methods', loc='upper right')

# Show the plot
plt.show()
