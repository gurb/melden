from OpenGL.GL import *
import glm

class Renderer:
    def __init__(self):
        pass

    def clear(self):
        glClearColor(.4, 0.1, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def render(self, shader, entity):
        shader.use()  

        e = entity
        model = entity.model
        glBindVertexArray(model.vao)

        transform = glm.identity(glm.mat4x4)
        transform = glm.translate(transform, glm.vec3(e.pos.x, e.pos.y, e.pos.z))
        transform = glm.rotate(transform, glm.radians(e.angle_x), glm.vec3(1, 0, 0)) # x-axis
        transform = glm.rotate(transform, glm.radians(e.angle_y), glm.vec3(0, 1, 0)) # y-axis
        transform = glm.rotate(transform, glm.radians(e.angle_z), glm.vec3(0, 0, 1)) # z-axis
        transform = glm.scale(transform, glm.vec3(e.scale.x, e.scale.y, e.scale.z))

        shader.setMatrix4f("mat_transform", transform)  

        glDrawArrays(GL_TRIANGLES, 0, model.vertex_count)
