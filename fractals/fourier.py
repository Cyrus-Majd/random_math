import matplotlib.pyplot as plt
import numpy as np
import cv2

# returns coords of triangle dots
def gen_triangle():
    # Define the side length of the equilateral triangle
    side_length = 1.0

    # Calculate the height of the equilateral triangle
    height = (3 ** 0.5) / 2 * side_length

    # Define the three vertices of the equilateral triangle
    vertices = np.array([
        [0, 0],
        [side_length, 0],
        [side_length / 2, height]
    ])

    # Create an array of 30 equidistant points on the perimeter of the triangle
    num_points = 30
    equidistant_points = []

    # Points along the first edge
    for i in range(num_points):
        t = i / (num_points - 1)  # Parameterization from 0 to 1
        x = (1 - t) * vertices[0][0] + t * vertices[1][0]
        y = (1 - t) * vertices[0][1] + t * vertices[1][1]
        equidistant_points.append([x, y])

    # Points along the second edge
    for i in range(num_points):
        t = i / (num_points - 1)  # Parameterization from 0 to 1
        x = (1 - t) * vertices[1][0] + t * vertices[2][0]
        y = (1 - t) * vertices[1][1] + t * vertices[2][1]
        equidistant_points.append([x, y])

    # Points along the third edge
    for i in range(num_points):
        t = i / (num_points - 1)  # Parameterization from 0 to 1
        x = (1 - t) * vertices[2][0] + t * vertices[0][0]
        y = (1 - t) * vertices[2][1] + t * vertices[0][1]
        equidistant_points.append([x, y])

    # Convert the equidistant points to a numpy array
    equidistant_points = np.array(equidistant_points)

    # Plot the equilateral triangle
    triangle = plt.Polygon(vertices, closed=True, fill=None, edgecolor='b')
    plt.gca().add_patch(triangle)

    # Plot the equidistant points on the triangle
    plt.scatter(equidistant_points[:, 0], equidistant_points[:, 1], c='r', label='Equidistant Points')

    # Set axis limits
    plt.xlim(-0.1, side_length + 0.1)
    plt.ylim(-0.1, height + 0.1)

    # Add labels
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Equilateral Triangle with Equidistant Points on the Perimeter')

    # Show the plot
    plt.legend()
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return equidistant_points

def transform(coordinates):

    # Extract x and y values
    x_values, y_values = zip(*coordinates)

    # Perform the Discrete Fourier Transform (DFT)
    dft = np.fft.fft(y_values)

    # Limit the number of terms (choose a small value for "num_terms")
    num_terms = 10000  # Adjust this to control the "squigglyness"

    # Set the higher frequency components to zero to reduce the number of terms
    dft[num_terms:] = 0

    # Generate the reconstructed curve from the modified DFT
    reconstructed_curve = np.fft.ifft(dft)

    # Visualize the original data and the reconstructed curve
    plt.scatter(x_values, y_values, label="Original Data")
    plt.plot(x_values, reconstructed_curve, label="Reconstructed Curve", color="red")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.title(f"sus thing for terms = {num_terms}")
    plt.show()

    # for i in range(5, 100, 5):
    #     print(i)

    #     # Perform the Discrete Fourier Transform (DFT)
    #     dft = np.fft.fft(y_values)

    #     # Limit the number of terms (choose a small value for "num_terms")
    #     num_terms = i  # Adjust this to control the "squigglyness"

    #     # Set the higher frequency components to zero to reduce the number of terms
    #     dft[num_terms:] = 0

    #     # Generate the reconstructed curve from the modified DFT
    #     reconstructed_curve = np.fft.ifft(dft)

    #     # Visualize the original data and the reconstructed curve
    #     plt.scatter(x_values, y_values, label="Original Data")
    #     plt.plot(x_values, reconstructed_curve, label="Reconstructed Curve", color="red")
    #     plt.xlabel("X")
    #     plt.ylabel("Y")
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()

def extract_coords_from_pic():

    # Load the image
    image = cv2.imread('s3.jpg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define Canny edge detection thresholds
    threshold1 = 100
    threshold2 = 200

    # Apply Canny edge detection
    edges = cv2.Canny(gray, threshold1, threshold2)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Extract coordinates from the contours
    coordinates = []
    for contour in contours:
        for point in contour:
            x, y = point[0]
            coordinates.append((x, y))

    # Now, the 'coordinates' list contains the (x, y) coordinates of edge points

    # You can further process and analyze these coordinates as needed

    return coordinates

def works():

    # equidistant_points = gen_triangle()
    equidistant_points = extract_coords_from_pic()

    print(equidistant_points)

    transform(equidistant_points)

def prev():

    # Load the image
    image = cv2.imread('liberty.jpg', cv2.IMREAD_GRAYSCALE)

    # Perform Canny edge detection
    edges = cv2.Canny(image, 100, 200)

    # Perform 2D Fourier Transform
    f_transform = np.fft.fft2(edges)
    f_transform_shifted = np.fft.fftshift(f_transform)
    magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)

    # Extract the central region (low-frequency components)
    rows, cols = magnitude_spectrum.shape
    center_rows, center_cols = rows // 2, cols // 2
    magnitude_spectrum = magnitude_spectrum[center_rows - 50:center_rows + 50, center_cols - 50:center_cols + 50]

    # Fit the data with 10 polynomials using NumPy's polyfit
    x = np.linspace(-50, 49, 100)
    y = np.linspace(-50, 49, 100)
    X, Y = np.meshgrid(x, y)
    coefficients = np.polyfit(X.ravel(), Y.ravel(), 10)

    # Print the coefficients of the 10 polynomials
    print(coefficients)

    # Visualize the magnitude spectrum and edge image
    plt.subplot(121), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Fourier Transform Magnitude Spectrum')
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image')
    plt.show()



works()