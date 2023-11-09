import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *  # Import gluPerspective
import math

# Define Hilbert curve function (similar to 2D version)
def hilbert_curve(order, angle, depth):
    if depth == 0:
        return []

    angle *= -1
    sub_curve = hilbert_curve(order, angle, depth - 1)

    return (
        sub_curve
        + [angle]
        + sub_curve
        + [angle]
        + [0]
        + sub_curve
        + [-angle]
        + [0]
        + [angle]
        + sub_curve
        + [0]
        + [-angle]
        + sub_curve
    )

# Convert the curve data to 3D points
def points_from_curve(order, angle, depth):
    curve_data = hilbert_curve(order, angle, depth)
    points = [(0, 0, 0)]
    current_x, current_y, current_z = 0, 0, 0
    current_angle = 0

    for step in curve_data:
        if step == 0:
            current_x += math.cos(math.radians(current_angle))
            current_y += math.sin(math.radians(current_angle))
        else:
            current_angle += step
        points.append((current_x, current_y, current_z))

    return points

# Initialize Pygame
pygame.init()
display = (1800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Draw the 3D Hilbert curve
def draw_hilbert_curve(order, angle, depth):
    points = points_from_curve(order, angle, depth)

    glBegin(GL_LINES)
    for i in range(1, len(points)):
        glVertex3fv(points[i - 1])
        glVertex3fv(points[i])
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(.1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_hilbert_curve(3, 90, 3)
    pygame.display.flip()
    pygame.time.wait(10)
