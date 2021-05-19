import pygame
from pygame.math import Vector3
from OpenGL.GL import *
import numpy as np
from ctypes import sizeof, c_void_p
from random import randint, uniform
import glm

from shaders.ShaderProgram import *
from Mesh import *

from Renderer import *
from Entity import *
from Light import *
from Camera import *
from Cube import *

class App:
    def __init__(self):
        pygame.init()
        self.width = 1440
        self.height = 900
        self.display = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF|pygame.OPENGL)
        self.clock = pygame.time.Clock()
        self.running = True
        self.generate()

    def generate(self):
        self.shader = ShaderProgram("./shaders/vs.glsl", "./shaders/fs.glsl")
        self.shader.addUniform("screen_dim")
        self.shader.addUniform("mat_transform")
        self.shader.addUniform("mat_projection")
        self.shader.addUniform("mat_view")
        

        self.cubeShader =  ShaderProgram("./shaders/cube_vs.glsl", "./shaders/cube_fs.glsl")
        self.cubeShader.addUniform("mat_transform")
        self.cubeShader.addUniform("mat_projection")
        self.cubeShader.addUniform("mat_view")

        # self.lightShader = ShaderProgram("./shaders/light_vs.glsl", "./shaders/light_fs.glsl")
        # self.lightShader.addUniform("mat_transform")
        # self.lightShader.addUniform("mat_view")
        # self.lightShader.addUniform("mat_projection")
        # self.lightShader.addUniform("objectColor")
        # self.lightShader.addUniform("lightColor")

        self.shaders = [
            self.shader,
            self.cubeShader
        ]

        self.meshes = []

        self.renderer = Renderer(self.shaders)
        

        self.pos = glm.vec2(0,0)
        self.angle = 0

        self.transform = glm.identity(glm.mat3x3)

        self.model = Mesh((-1.0, -0.0), (.3,.3), "./res/image.png")
        self.cube_model = Cube()
        # self.light_model = Light(0.5)
    
        self.e = Entity(self.model, Vector3(0,0,0), Vector3(0.0,0.0,0.0), Vector3(1,1,1))
        self.shadersDict = {
            self.e : [self.shader, False],
        }
        precision = 3
        self.cube_entities = []
        for i in range(1000):
            x = round(uniform(-10, 10), precision)
            y = round(uniform(-10, 10), precision)
            z = round(uniform(-10, 10), precision)
            self.cube_entities.append(Entity(self.cube_model, Vector3(x,y,z), Vector3(0.0,0.0,0.0), Vector3(0.5,0.5,0.5))) 
            self.shadersDict[self.cube_entities[i]] = [self.cubeShader, True]    

        # self.cube_entities = Entity(self.cube_model, Vector3(0,0,0), Vector3(0.0,0.0,0.0), Vector3(1,1,1))

        self.camera = Camera()
        # precision = 3
        # self.angle = 0
        # for e in range(50):
        #     x = round(uniform(-1, 1), precision)
        #     y = round(uniform(-1, 1), precision)
        #     z = round(uniform(-1, 1), precision)
        #     self.entities.append(Entity(self.model, Vector3(x,y,0), Vector3(0.0,0.0,0.0), Vector3(x,y,.1)))        
        
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

        self.camera.move()

        # self.lightShader.use()
        # self.light_e.model.draw()
        
        
        for e in self.cube_entities:    
            e.rotate(3,5,3)


        self.camera.update(self.shaders)

        self.renderer.render(self.shadersDict)
