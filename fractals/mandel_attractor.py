import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# Define the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iterations = 256

# Create an empty image with the specified dimensions for the Mandelbrot set
mandelbrot_img = np.zeros((width, height))

# Create an empty image with the same dimensions for the Lorenz attractor
attractor_img = np.zeros((width, height))

# Define the Lorenz attractor function
def lorenz_attractor(x, y, z):
    sigma = 10
    rho = 28
    beta = 8/3
    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z
    return x + x_dot, y + y_dot, z + z_dot

# Generate the Lorenz attractor
x, y, z = 0.1, 0.0, 0.0
scale_factor = 1.0  # Initial scale factor
max_scale = 100.0   # Maximum scale factor to prevent divergence
for _ in range(width * height):
    x, y, z = lorenz_attractor(x, y, z)
    
    # Check if the values exceed a reasonable range
    if abs(x) > max_scale or abs(y) > max_scale:
        # Scale down the values if they exceed the maximum scale
        x *= scale_factor
        y *= scale_factor
        z *= scale_factor

    x_pixel = int((x - x_min) / (x_max - x_min) * width)
    y_pixel = int((y - y_min) / (y_max - y_min) * height)
    
    # Check if the pixel coordinates are valid
    if 0 <= x_pixel < width and 0 <= y_pixel < height:
        attractor_img[x_pixel, y_pixel] = 1
        scale_factor *= 1.001  # Gradually increase the scale factor to explore more space
        scale_factor = min(scale_factor, max_scale)  # Ensure the scale factor doesn't exceed the maximum



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
        mandelbrot_img[x, y] = i

# Combine the Mandelbrot fractal with the Lorenz attractor
combined_img = mandelbrot_img + attractor_img

# Display the combined image
plt.imshow(combined_img, extent=(x_min, x_max, y_min, y_max), cmap='hot', origin='lower')
plt.colorbar()
plt.show()
