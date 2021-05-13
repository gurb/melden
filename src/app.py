import pygame
from pygame.math import Vector3
from OpenGL.GL import *
import numpy as np
from ctypes import sizeof, c_void_p
from random import randint, uniform
import glm

from src.shaders.ShaderProgram import *
from src.Mesh import *

from src.Renderer import *
from src.Entity import *

class App:
    def __init__(self):
        pygame.init()
        self.width = 1280
        self.height = 720
        self.display = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF|pygame.OPENGL)
        self.clock = pygame.time.Clock()
        self.running = True
        self.generate()

    def generate(self):
        self.renderer = Renderer()
        
        self.shader = ShaderProgram("./src/shaders/vs.glsl", "./src/shaders/fs.glsl")
        self.shader.addUniform("screen_dim")
        self.shader.addUniform("mat_transform")
        self.meshes = []

        self.pos = glm.vec2(0,0)
        self.angle = 0

        self.transform = glm.identity(glm.mat3x3)

        self.model = Mesh((-1.0, -0.0), (.3,.3), "./src/res/image.png")

        self.entities = []
        precision = 3
        self.angle = 0
        for e in range(50):
            x = round(uniform(-1, 1), precision)
            y = round(uniform(-1, 1), precision)
            z = round(uniform(-1, 1), precision)
            self.entities.append(Entity(self.model, Vector3(x,y,0), Vector3(0.0,0.0,0.0), Vector3(x,y,.1)))        
        
    def execute(self):
        while self.running:
            self.handler_key()
            self.render()
            self.update()
        pygame.quit()

    def handler_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pygame.display.flip()

    def render(self):
        self.dt = self.clock.tick(60) / 1000
        glViewport(0, 0, self.width, self.height)
        self.renderer.clear()
    
        self.angle = 3
        for e in self.entities:    
            e.rotate(0,0,self.angle)
            self.renderer.render(self.shader, e)



