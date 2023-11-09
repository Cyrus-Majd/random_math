import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
num_iterations = 1000  # Total number of iterations for each parameter value
num_parameter_values = 1000  # Number of parameter values to explore
parameter_range = (2.4, 4.0)  # Range of parameter values (common for the logistic map)

# Create an array of parameter values
parameter_values = np.linspace(parameter_range[0], parameter_range[1], num_parameter_values)

# Initialize an array to store the bifurcation diagram data
bifurcation_data = []

# Iterate through different parameter values
for r in parameter_values:
    x = 0.5  # Initial value of x
    for _ in range(num_iterations):
        x = logistic_map(r, x)
        if _ >= (num_iterations - 20):  # Capture the last 20 iterations
            bifurcation_data.append((r, x))

# Extract and separate the parameter and x values
parameter_values = [data[0] for data in bifurcation_data]
x_values = [data[1] for data in bifurcation_data]

# Plot the bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(parameter_values, x_values, s=1, c='b', marker='x', edgecolors='none', label = "EPIC DATA POINTS")
plt.title("math leaf (the leaf that is math)")
plt.xlabel("numbner")
plt.ylabel("other number")
plt.legend(loc='lower left', labelcolor='blue')
# plt.legend("the math points of the leaf which is math")
plt.xlim(parameter_range)
plt.show()
