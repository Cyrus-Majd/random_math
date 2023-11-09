import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrate_one_to_two():
    # Define a list of exponents
    exponents = np.linspace(1.0, 2.0, 11)  # Ranging from 1.0 to 2.0 in increments of 0.1

    # Initialize lists to store results
    results = []
    x_values = np.linspace(0, 5, 1000)

    # Calculate integrals and plot each function
    for exponent in exponents:
        def function(x):
            return x**exponent

        result, _ = quad(function, 0, 5)
        results.append(result)

        y_values = [function(x) for x in x_values]
        plt.plot(x_values, y_values, label=f'x^{exponent}')

    # Plot the results
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Integrals of x^1 to x^2')
    plt.legend()
    plt.show()

    # Print the calculated results
    for exponent, result in zip(exponents, results):
        print(f'Integral of x^{exponent} from 0 to 5: {result}')

def integrate_two_to_three():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import quad

    # Define a list of exponents
    exponents = np.linspace(2.0, 3.0, 11)  # Ranging from 2.0 to 3.0 in increments of 0.1

    # Initialize lists to store results
    results = []
    x_values = np.linspace(0, 5, 1000)

    # Calculate integrals and plot each function
    for exponent in exponents:
        def function(x):
            return x**exponent

        result, _ = quad(function, 0, 5)
        results.append(result)

        y_values = [function(x) for x in x_values]
        plt.plot(x_values, y_values, label=f'x^{exponent}')

    # Plot the results
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Integrals of x^2 to x^3')
    plt.legend()
    plt.show()

    # Print the calculated results
    for exponent, result in zip(exponents, results):
        print(f'Integral of x^{exponent} from 0 to 5: {result}')

def function(x):
    return x**2

def two_d_visualization():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Create an array of x values
    x_values = np.linspace(0, 5, 100)
    y_values = [function(x) for x in x_values]

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the range of integration
    x_range = np.linspace(0, 5, 100)
    y_range = np.zeros_like(x_range)
    z_range = [function(x) for x in x_range]

    # Extrude the square along the x-axis
    ax.plot(x_range, y_range, z_range, linewidth=2)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Visualization of Extruding Square for ∫[0 to 5] x^2 dx')

    plt.show()

def extruding_square():
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    from scipy.integrate import quad

    # Create a figure and a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the vertices of the square at the base
    x = [0, 5, 5, 0, 0]
    y = [0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0]

    # Plot the initial square
    square = [list(zip(x, y, z))]
    ax.add_collection3d(Poly3DCollection(square, color='b', alpha=0.5))

    # Integration
    integrated_volume = quad(function, 0, 5)[0]

    # Create the vertices of the extruded cube
    x_cube = [0, 5, 5, 0, 0, 0, 5, 5, 5, 0, 0, 5, 5, 0, 0, 0]
    y_cube = [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0]
    z_cube = [0, 0, integrated_volume, integrated_volume, 0, 0, 0, 0, integrated_volume, integrated_volume, integrated_volume, integrated_volume, integrated_volume, integrated_volume, integrated_volume, integrated_volume]

    # Plot the extruded cube
    cube = [list(zip(x_cube, y_cube, z_cube))]
    ax.add_collection3d(Poly3DCollection(cube, color='r', alpha=0.5))

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Set the plot limits
    ax.set_xlim([0, 5])
    ax.set_ylim([0, 5])
    ax.set_zlim([0, integrated_volume])

    # Show the plot
    plt.title('3D Visualization: Integration of x^2 (Square Extruded into Cube)')
    plt.show()

    # Print the value of the integral
    print(f"The integral of x^2 from 0 to 5: {integrated_volume}")

def seirpinsky():
    import matplotlib.pyplot as plt

# Define function to generate the Sierpinski Triangle
def sierpinski(x, y, size, depth):
    if depth == 0:
        # Draw an equilateral triangle
        plt.fill(x, y, 'b')
    else:
        # Calculate midpoints of the sides
        mid1 = [(x[0] + x[1]) / 2, (y[0] + y[1]) / 2]
        mid2 = [(x[1] + x[2]) / 2, (y[1] + y[2]) / 2]
        mid3 = [(x[0] + x[2]) / 2, (y[0] + y[2]) / 2]

        # Recursively draw smaller triangles
        sierpinski([x[0], mid1[0], mid3[0]], [y[0], mid1[1], mid3[1]], size / 2, depth - 1)
        sierpinski([mid1[0], x[1], mid2[0]], [mid1[1], y[1], mid2[1]], size / 2, depth - 1)
        sierpinski([mid3[0], mid2[0], x[2]], [mid3[1], mid2[1], y[2]], size / 2, depth - 1)

def draw_sierpinski():
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Initial triangle vertices
    initial_x = [0, 10, 5]
    initial_y = [0, 0, 8]

    # Set the depth of recursion (adjust for desired level of detail)
    depth = 4

    # Call the Sierpinski function to generate the fractal
    sierpinski(initial_x, initial_y, 10, depth)

    # Set axis limits and aspect ratio
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')

    # Remove axis labels and ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Show the Sierpinski Triangle
    plt.show()





# integrate_one_to_two()
# integrate_two_to_three()
# two_d_visualization()
# extruding_square()
# draw_sierpinski()
# extruded_sierpinski()