import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROTATION_SPEED = 1.0  # Degrees per frame
NUM_SUBDIVISIONS = 3

# Vertex shader
vertex_shader = """
#version 330 core

layout(location = 0) in vec4 position;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * position;
}
"""

# Fragment shader
fragment_shader = """
#version 330 core

out vec4 FragColor;
uniform vec3 objectColor;
uniform vec3 lightColor;

void main()
{
    FragColor = vec4(objectColor * lightColor, 1.0);
}
"""

# Compile shader source
def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader)
        print("Shader compilation failed:", error)
        glDeleteShader(shader)
        return None

    return shader

# Create a cube
def create_cube(vertices):
    vertices = [
        -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1,
        -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1,
        -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1,
        -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1,
        -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1,
        -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, 1
    ]
    
    for vertex in vertices:
        glVertex3fv(vertices[vertex * 3:vertex * 3 + 3])

# Main loop
def main():
    # Initialize the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Create and compile the shaders
    vertex_shader_id = compile_shader(vertex_shader, GL_VERTEX_SHADER)
    fragment_shader_id = compile_shader(fragment_shader, GL_FRAGMENT_SHADER)

    # Create and link the shader program
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader_id)
    glAttachShader(shader_program, fragment_shader_id)
    glLinkProgram(shader_program)
    glUseProgram(shader_program)

    # Set up lighting properties
    object_color = glGetUniformBlockIndex(shader_program, "objectColor")
    glUniformBlockBinding(shader_program, object_color, 0)
    object_color_buffer = glGenBuffers(1)
    glBindBufferBase(GL_UNIFORM_BUFFER, 0, object_color_buffer)
    glBufferData(GL_UNIFORM_BUFFER, 24, None, GL_DYNAMIC_DRAW)
    light_color = glGetUniformBlockIndex(shader_program, "lightColor")
    glUniformBlockBinding(shader_program, light_color, 1)
    light_color_buffer = glGenBuffers(1)
    glBindBufferBase(GL_UNIFORM_BUFFER, 1, light_color_buffer)
    glBufferData(GL_UNIFORM_BUFFER, 24, None, GL_DYNAMIC_DRAW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(ROTATION_SPEED, 1, 1, 0)  # Rotate the view
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_DEPTH_TEST)

        # Set cube properties
        object_color_data = (1.0, 0.5, 0.31)  # Object color (orange)
        light_color_data = (1.0, 1.0, 1.0)  # Light color (white)

        # Update uniform buffer data
        glBindBuffer(GL_UNIFORM_BUFFER, object_color_buffer)
        glBufferSubData(GL_UNIFORM_BUFFER, 0, 24, object_color_data)
        glBindBuffer(GL_UNIFORM_BUFFER, light_color_buffer)
        glBufferSubData(GL_UNIFORM_BUFFER, 0, 24, light_color_data)

        glBegin(GL_TRIANGLES)
        create_cube(vertices)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
