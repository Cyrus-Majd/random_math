import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from pyrr import Matrix44
import math

# Global variables for camera controls
zoom_factor = 1.0
rotation_angle_x = 0
rotation_angle_y = 0
rotation_angle_z = 0

# Flags for continuous rotation
rotate_left = False
rotate_right = False

vertices = [
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.5, 0.866, 0.0],
    [0.5, 0.289, 0.816]
]

edges = (
    (0, 1),
    (1, 2),
    (2, 0),
    (0, 3),
    (1, 3),
    (2, 3)
)

def draw_tetrahedron(vertices):
    glBegin(GL_TRIANGLES)

    def draw_face(a, b, c):
        glVertex3fv(vertices[a])
        glVertex3fv(vertices[b])
        glVertex3fv(vertices[c])

    # Front face
    draw_face(0, 1, 2)

    # Left face
    draw_face(0, 2, 3)

    # Right face
    draw_face(0, 3, 1)

    # Bottom face
    draw_face(1, 3, 2)

    glEnd()

def set_projection_matrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glLoadMatrixf(Matrix44.perspective_projection(45.0, 800/600, 0.1, 50.0).flatten())

def sierpinski_tetrahedron(vertices, depth):
    if depth == 0:
        draw_tetrahedron(vertices)
    else:
        mid01 = [(vertices[0][i] + vertices[1][i]) / 2 for i in range(3)]
        mid02 = [(vertices[0][i] + vertices[2][i]) / 2 for i in range(3)]
        mid03 = [(vertices[0][i] + vertices[3][i]) / 2 for i in range(3)]
        mid12 = [(vertices[1][i] + vertices[2][i]) / 2 for i in range(3)]
        mid23 = [(vertices[2][i] + vertices[3][i]) / 2 for i in range(3)]
        mid13 = [(vertices[1][i] + vertices[3][i]) / 2 for i in range(3)]

        sierpinski_tetrahedron([vertices[0], mid01, mid02, mid03], depth - 1)
        sierpinski_tetrahedron([mid01, vertices[1], mid12, mid13], depth - 1)
        sierpinski_tetrahedron([mid02, mid12, vertices[2], mid23], depth - 1)
        sierpinski_tetrahedron([mid03, mid13, mid23, vertices[3]], depth - 1)

def main():
    global zoom_factor, rotation_angle_x, rotation_angle_y, rotation_angle_z
    global rotate_left, rotate_right

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    set_projection_matrix()
    glTranslatef(0, 0, -3)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zoom_factor += 0.1
                elif event.key == pygame.K_DOWN:
                    zoom_factor -= 0.1
                elif event.key == pygame.K_a:
                    rotate_left = True
                elif event.key == pygame.K_d:
                    rotate_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    rotate_left = False
                elif event.key == pygame.K_d:
                    rotate_right = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    zoom_factor += 0.1
                elif event.button == 5:  # Scroll down
                    zoom_factor -= 0.1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rotation_angle_y += 1
        if keys[pygame.K_RIGHT]:
            rotation_angle_y -= 1

        if rotate_left:
            rotation_angle_z += 1
        if rotate_right:
            rotation_angle_z -= 1

        glPushMatrix()
        glRotatef(rotation_angle_x, 1, 0, 0)
        glRotatef(rotation_angle_y, 0, 1, 0)
        glRotatef(rotation_angle_z, 0, 0, 1)
        glScalef(zoom_factor, zoom_factor, zoom_factor)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        sierpinski_tetrahedron(vertices, depth=3)
        pygame.display.flip()
        pygame.time.wait(10)
        glPopMatrix()

if __name__ == "__main__":
    main()
