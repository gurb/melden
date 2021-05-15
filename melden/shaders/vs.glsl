#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;

out vec2 passTexCoords;

uniform mat4 mat_transform;
uniform mat4 mat_projection;
uniform mat4 mat_view;

void main(){
    gl_Position = mat_projection * mat_view * mat_transform * vec4(position, 1.0);
    passTexCoords = texCoords;
}