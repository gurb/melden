from OpenGL.GL import *

class Triangle:
    def __init__(self):
        self.VAO = glGenVertexArrays(1)
    
    def bind(self):
        glBindVertexArray(self.VAO)

    def unbind(self):
        glBindVertexArray(0)

