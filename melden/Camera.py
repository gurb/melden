import pygame
import glm
from OpenGL.GL import *
from pygame.math import Vector3 as Vec3
from pygame.key import get_pressed

'''
Camera attributes:
a. Position of camera (x,y,z)
b. Aircraft principal axes:
    1. roll: left and right roll action by the front-to-back axis
    2. pitch: up-and-down movement by side-to-side axis
    3. yaw: defining of the direction by vertical axis
c. view matrix
    it's camera matrix
d. velocity of camera movement: vel
'''
class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        self.roll = None
        self.pitch = None
        self.yaw = None
        
        self.viewMatrix = None

        self.vel = 0.002

        self.offsetCamera = glm.vec3(-self.x, -self.y, -self.z)

    def move(self):
        keys = get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.z -= self.vel
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x -= self.vel
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.x += self.vel
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.z -= self.vel

    def getView(self): 
        self.viewMatrix = glm.identity(glm.mat4x4)
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.pitch), glm.vec3(1, 0, 0)) # x-axis
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.yaw), glm.vec3(0, 1, 0)) # y-axis
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.roll), glm.vec3(0, 0, 1)) # z-axis
        self.offsetCamera = glm.vec3(-self.x, -self.y, -self.z)
        self.viewMatrix = glm.translate(self.viewMatrix, self.offsetCamera)
        self.viewMatrix = glm.scale(transform, glm.vec3(e.scale.x, e.scale.y, e.scale.z))
        return self.viewMatrix