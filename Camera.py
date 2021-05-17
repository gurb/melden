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

        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        
        self.viewMatrix = None

        self.vel = 0.03

        self.offsetCamera = glm.vec3(-self.x, -self.y, -self.z)

    def move(self):
        keys = get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_w]:
            self.z -= self.vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x -= self.vel
        if keys[pygame.K_UP] or keys[pygame.K_a]:
            self.x += self.vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.z += self.vel

    def getView(self): 
        self.viewMatrix = glm.identity(glm.mat4x4)
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.pitch), glm.vec3(1, 0, 0)) # x-axis
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.yaw), glm.vec3(0, 1, 0)) # y-axis
        self.viewMatrix = glm.rotate(self.viewMatrix, glm.radians(self.roll), glm.vec3(0, 0, 1)) # z-axis
        self.offsetCamera = glm.vec3(-self.x, -self.y, -self.z)
        self.viewMatrix = glm.translate(self.viewMatrix, self.offsetCamera)
        return self.viewMatrix

    def update(self, shaders):
        for shader in shaders:
            shader.setMatrix4f("mat_view", self.getView())