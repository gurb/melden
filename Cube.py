import pygame
from OpenGL.GL import *
import numpy
from ctypes import sizeof, c_void_p

class Cube:
    def __init__(self):
        self.vertices = [
            -0.5, -0.5,  0.5, 0.0, 0.0, 1.0,
             0.5, -0.5,  0.5, 1.0, 1.0, 0.0,
             0.5,  0.5,  0.5, 0.0, 0.1, 0.0,
            -0.5,  0.5,  0.5, 1.0, 0.0, 0.0,

            -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 1.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 1.0, 0.0,
            -0.5,  0.5, -0.5, 0.0, 0.0, 1.0,
        ]

        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)

        self.indices = [
            0, 1, 2, 2, 3, 0,
            4, 5, 6, 6, 7, 4,
            4, 5, 1, 1, 0, 4,
            6, 7, 3, 3, 2, 6,
            5, 6, 2, 2, 1, 5,
            7, 4, 0, 0, 3, 7
        ]
        self.indices_len = 36
        self.indices = numpy.array(self.indices, dtype=numpy.uint32)

        self.vao = glGenVertexArrays(1)        
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, 192, self.vertices, GL_STATIC_DRAW)

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, 144, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, c_void_p(12))

    def draw(self):
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, None)
