import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

def default_lorenz():

    # Lorenz system parameters
    sigma = 1
    rho = 50
    beta = 10

    # Time parameters
    dt = 0.001
    num_steps = 100000

    # Initial conditions
    x, y, z = 0.8, 60, 0

    # Arrays to store the trajectory
    x_values = [x]
    y_values = [y]
    z_values = [z]

    # Numerical integration using the Lorenz equations
    for _ in range(num_steps):
        dx = sigma * (y - x) * dt
        dy = (x * (rho - z) - y) * dt
        dz = (x * y - beta * z) * dt

        x += dx
        y += dy
        z += dz

        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

    # Create a 3D plot of the Lorenz attractor
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_values, y_values, z_values, lw=0.5)
    ax.set_title('Lorenz Attractor')

    plt.show()

def lorenz_with_slidebar():

    # Lorenz system parameters
    sigma = 10
    rho = 28
    beta = 8/3

    # Time parameters
    dt = 0.01
    num_steps = 10000

    # Initial conditions
    initial_x = 0.1
    initial_y = 0
    initial_z = 0

    # Create a figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('Lorenz Attractor')

    # Create a slider axes
    axcolor = 'lightgoldenrodyellow'
    ax_x = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor=axcolor)
    ax_y = plt.axes([0.2, 0.06, 0.65, 0.03], facecolor=axcolor)
    ax_z = plt.axes([0.2, 0.11, 0.65, 0.03], facecolor=axcolor)

    # Create sliders
    s_x = Slider(ax_x, 'X', 0, 1.0, valinit=initial_x)
    s_y = Slider(ax_y, 'Y', 0, 1.0, valinit=initial_y)
    s_z = Slider(ax_z, 'Z', 0, 1.0, valinit=initial_z)

    # Arrays to store the trajectory
    x_values = [initial_x]
    y_values = [initial_y]
    z_values = [initial_z]

    # Plot initialization
    line, = ax.plot(x_values, y_values, z_values, lw=0.5)

    # Function to update the plot based on slider values
    def update(val):
        x, y, z = s_x.val, s_y.val, s_z.val
        x_values[0] = x
        y_values[0] = y
        z_values[0] = z
        x_values.clear()
        y_values.clear()
        z_values.clear()
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
        for _ in range(num_steps):
            dx = sigma * (y - x) * dt
            dy = (x * (rho - z) - y) * dt
            dz = (x * y - beta * z) * dt
            x += dx
            y += dy
            z += dz
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)
        line.set_data(x_values, y_values)
        line.set_3d_properties(z_values)
        fig.canvas.draw_idle()

    s_x.on_changed(update)
    s_y.on_changed(update)
    s_z.on_changed(update)

    plt.show()


default_lorenz()