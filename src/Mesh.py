import pygame
from OpenGL.GL import *
import numpy
from ctypes import sizeof, c_void_p


class Mesh:
    def __init__(self, position, size, texture=None):
        self.textureID = self.load_texture(texture)
        
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0, 0.25, 0.75,
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0, 0.75, 0.75,
             0.0,  0.5, 0.0, 0.0, 0.0, 1.0, 0.50, 0.25 
        )
        self.vertex_count = 8
        self.vertices = numpy.array(self.vertices, dtype=numpy.float32)

        self.vao = glGenVertexArrays(1)        
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        v_size = [3,3,2] # (x,y,z) (r,g,b) (s,t)
        for loc in range(3):
            glEnableVertexAttribArray(loc)
            glVertexAttribPointer(loc, v_size[loc], GL_FLOAT, GL_FALSE, 8*4, c_void_p(loc * v_size[loc] * 4))

    # def draw(self):
    #     glBindTexture(GL_TEXTURE_2D, self.textureID)
    #     glBindVertexArray(self.vao)
    #     glDrawArrays(GL_TRIANGLES, 0, 3)
        
    def load_texture(self, path):
        textureId = glGenTextures(1)
        # if we use texture object then we need to activate the object.
        glBindTexture(GL_TEXTURE_2D, textureId)
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        tex_image  = pygame.image.load(path)
        tex_data   = pygame.image.tostring(tex_image, "RGB", 1)
        tex_width  = tex_image.get_width()
        tex_height = tex_image.get_height()

        glTexImage2D(
            GL_TEXTURE_2D, 
            0,
            GL_RGB,
            tex_width,
            tex_height,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            tex_data
        )

        return textureId