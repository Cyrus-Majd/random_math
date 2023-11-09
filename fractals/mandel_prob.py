import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iterations = 512

# Create an empty image with the specified dimensions
img = np.zeros((width, height))

# Generate the Mandelbrot fractal
for x in range(width):
    for y in range(height):
        real_part = x_min + (x / (width - 1)) * (x_max - x_min)
        imag_part = y_min + (y / (height - 1)) * (y_max - y_min)

        z = complex(0, 0)
        c = complex(real_part, imag_part)

        for i in range(max_iterations):
            if abs(z) > 2.0:
                break
            z = z * z + c

        # Color the pixel based on the number of iterations
        img[x, y] = i

# Display the Mandelbrot fractal using Matplotlib
plt.imshow(img, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
plt.colorbar()
plt.show()
