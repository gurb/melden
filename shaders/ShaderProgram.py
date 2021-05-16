from OpenGL.GL import *
import glm

class ShaderProgram:
    def __init__(self, vs_path, fs_path):
        self.programID = glCreateProgram()
        self.shaders = []
        self.addShader(vs_path, GL_VERTEX_SHADER)
        self.addShader(fs_path, GL_FRAGMENT_SHADER)
        self.uniforms = dict()
        self.link()

    def addShader(self, shaderSourcePath, shaderType):
        shaderID = glCreateShader(shaderType)
        self.shaders.append(shaderID)
        sourceCode = self.read_file(shaderSourcePath)
        glShaderSource(shaderID, sourceCode)
        glCompileShader(shaderID)
        
        if glGetShaderiv(shaderID, GL_COMPILE_STATUS) != GL_TRUE:
            infoLog = glGetShaderInfoLog(shaderID)
            raise Exception("Failed to compile shader: {0}".format(infoLog))

        glAttachShader(self.programID, shaderID)
        glDeleteShader(shaderID)

    def link(self):
        glLinkProgram(self.programID)
        if glGetProgramiv(self.programID, GL_LINK_STATUS) != GL_TRUE:
            infoLog = glGetProgramInfoLog(self.programID)
            raise RuntimeError("Failed to link program: {0}".format(infoLog))

    def use(self):
        glUseProgram(self.programID)

    def bindAttribute(self, attribute:int, varName:str):
        glBindAttribLocation(self.programID, attribute, varName)

    def addUniform(self, uniformName):
        self.uniforms[uniformName] = glGetUniformLocation(self.programID, uniformName)

    def setUniform2f(self, uniformName, value):
        glUniform2f(self.uniforms[uniformName], value.x, value.y)

    def setMatrix4f(self, uniformName, matrix4x4):
        glUniformMatrix4fv(self.uniforms[uniformName], 1, GL_FALSE, glm.value_ptr(matrix4x4))

    def read_file(self, path):
        with open(path) as f:
            text = f.read()
            f.close()
        return text

    def __del__(self):
        try:
            for shader in self.shaders:
                glDetachShader(self.programID, shader)
                glDeleteShader(shader)
            glDeleteProgram(self.program)
        except OpenGL.error.NullFunctionError as error:
            return Exception(error)            
