from OpenGL.GL import *
import glm

class Renderer:
    def __init__(self, shaders):
        self.fov = 70
        self.near_plane = 0.1
        self.far_plane = 5
        self.shaders = shaders

        for shader in self.shaders:
            shader.use()
            self.projectionMatrix = None
            self.getProjectionMatrix()
            shader.setMatrix4f("mat_projection", self.projectionMatrix)  

    def clear(self):
        glClearColor(.4, 0.1, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def render(self, shadersDict):
        for entity in shadersDict:
            shadersDict[entity][0].use()  

            e = entity
            model = entity.model
            glBindVertexArray(model.vao)

            transform = glm.identity(glm.mat4x4)
            transform = glm.translate(transform, glm.vec3(e.pos.x, e.pos.y, e.pos.z))
            transform = glm.rotate(transform, glm.radians(e.angle_x), glm.vec3(1, 0, 0)) # x-axis
            transform = glm.rotate(transform, glm.radians(e.angle_y), glm.vec3(0, 1, 0)) # y-axis
            transform = glm.rotate(transform, glm.radians(e.angle_z), glm.vec3(0, 0, 1)) # z-axis
            transform = glm.scale(transform, glm.vec3(e.scale.x, e.scale.y, e.scale.z))

            shadersDict[entity][0].setMatrix4f("mat_transform", transform)  

            if shadersDict[entity][1]:
                shadersDict[entity][0].setVec3("objectColor", 1.0, 0.5, 0.31)
                shadersDict[entity][0].setVec3("lightColor", 1.0, 1.0, 1.0)
                glDrawElements(GL_TRIANGLES, model.indices_len, GL_UNSIGNED_INT, 0)
            else:
                glDrawArrays(GL_TRIANGLES, 0, model.vertex_count)

    def getProjectionMatrix(self):
        self.projectionMatrix = glm.perspective(glm.radians(self.fov), float(1280/720), self.near_plane, self.far_plane)
        
