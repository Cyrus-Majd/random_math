import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

vertices = [
    (0.0, 1.0, 0.0),
    (1.0, 0.0, 0.0),
    (-1.0, 0.0, 0.0),
    (0.0, 0.0, 1.0),
]

edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)

# Vertex and fragment shaders
vertex_shader = """
#version 330 core
layout(location = 0) in vec3 position;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

fragment_shader = """
#version 330 core
out vec4 color;
void main() {
    color = vec4(0.0, 0.0, 0.0, 1.0);
}
"""

def create_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise Exception("Shader compilation failed: " + glGetShaderInfoLog(shader))
    return shader

def sierpinski_tetrahedron(vertices, depth):
    if depth == 0:
        for edge in edges:
            glBegin(GL_LINES)
            for vertex in edge:
                glVertex3fv(vertices[vertex])
            glEnd()
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
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    # Create shaders
    vertex_shader_id = create_shader(GL_VERTEX_SHADER, vertex_shader)
    fragment_shader_id = create_shader(GL_FRAGMENT_SHADER, fragment_shader)

    # Create shader program
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader_id)
    glAttachShader(shader_program, fragment_shader_id)
    glLinkProgram(shader_program)
    glUseProgram(shader_program)

    model_loc = glGetUniformLocation(shader_program, "model")
    view_loc = glGetUniformLocation(shader_program, "view")
    projection_loc = glGetUniformLocation(shader_program, "projection")

    glClearColor(1, 1, 1, 1)

    zoom_factor = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    zoom_factor += 0.1
                elif event.button == 5:  # Scroll down
                    zoom_factor -= 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        model = glGetFloatv(GL_MODELVIEW_MATRIX)
        view = glGetFloatv(GL_MODELVIEW_MATRIX)
        projection = glGetFloatv(GL_PROJECTION_MATRIX)

        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
        glUniformMatrix4fv(projection_loc, 1, GL_FALSE, projection)


        glRotatef(.1, 0, 0, 1)
        glScalef(zoom_factor, zoom_factor, zoom_factor)

        sierpinski_tetrahedron(vertices, depth=3)
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
