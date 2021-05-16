from pygame.math import Vector3

class Entity: 
    def __init__(self, model, pos, rot, scale):
        self.model = model
        self.pos = pos
        
        self.rot = rot        
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.set_angle()
        
        self.scale = scale

    def translate(self, x, y, z):
        self.pos.x += x
        self.pos.y += y
        self.pos.z += z
    
    def rotate(self, x, y, z):
        self.rot.x += x
        self.rot.y += y
        self.rot.z += z
        self.set_angle()

    def set_angle(self):
        if self.rot.x:  self.angle_x = self.rot.x
        if self.rot.y:  self.angle_y = self.rot.y
        if self.rot.z:  self.angle_z = self.rot.z

    def scale(self, x, y, z):
        self.scale.x += x
        self.scale.y += y
        self.scale.z += z