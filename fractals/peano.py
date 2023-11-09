import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
ROTATION_SPEED = .5  # Degrees per frame
NUM_SUBDIVISIONS = 1

# Initialize the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Define the Menger sponge algorithm
def menger_sponge(order, size, x, y, z):
    if order == 0:
        draw_cube(size, x, y, z)
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i == 1 and j == 1 and k == 1:
                        continue
                    menger_sponge(order - 1, new_size, x + i * new_size - size / 2, y + j * new_size - size / 2, z + k * new_size - size / 2)

# Function to draw a cube
def draw_cube(size, x, y, z):
    vertices = [
        [-size / 2, -size / 2, -size / 2],
        [size / 2, -size / 2, -size / 2],
        [size / 2, size / 2, -size / 2],
        [-size / 2, size / 2, -size / 2],
        [-size / 2, -size / 2, size / 2],
        [size / 2, -size / 2, size / 2],
        [size / 2, size / 2, size / 2],
        [-size / 2, size / 2, size / 2]
    ]

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv((vertices[vertex][0] + x, vertices[vertex][1] + y, vertices[vertex][2] + z))
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(ROTATION_SPEED, 1, 1, 0)  # Rotate the view
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menger_sponge(NUM_SUBDIVISIONS, 1.0, 0, 0, 0)
    pygame.display.flip()
    pygame.time.wait(10)
