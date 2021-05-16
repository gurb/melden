import pygame
from OpenGL.GL import *
import numpy
from ctypes import sizeof, c_void_p

class Cube:
    def __init__(self):
        self.pos = []
        self.vec


class Light:
    def __init__(self, len):
        self.vertices = [
            -len/2, -len/2, -len/2, 1.0, 0.0, 0.0, 1.0, # 0 
             len/2, -len/2, -len/2, 0.0, 1.0, 0.0, 1.0, # 1
             len/2, -len/2,  len/2, 0.0, 1.0, 1.0, 1.0, # 2
            -len/2, -len/2,  len/2, 0.0, 0.0, 1.0, 1.0, # 3

            -len/2,  len/2, -len/2, 1.0, 0.0, 0.0, 1.0, # 4
             len/2,  len/2, -len/2, 0.0, 1.0, 0.0, 1.0, # 5 
             len/2,  len/2,  len/2, 0.0, 1.0, 1.0, 1.0, # 6
            -len/2,  len/2,  len/2, 0.0, 0.0, 1.0, 1.0  # 7
        ]
        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)

        self.indices = [
            7, 3, 2,    7, 2, 6,    # front face (two triangles)
            6, 2, 1,    6, 1, 5,    # back face
            4, 7, 6,    4, 6, 5,    # top face
            0, 3, 2,    0, 2, 1,    # bottom face
            4, 0, 1,    4, 1, 5,    # right face
            7, 3, 0,    7, 0, 4     # left face
        ]
        self.indices = numpy.array(self.indices, dtype=numpy.uintc)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 7*4, c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 7*4, c_void_p(3*4))

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)