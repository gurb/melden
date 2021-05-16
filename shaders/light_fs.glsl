#version 330 core

out vec4 outColor;

uniform vec3 objectColor;
uniform vec3 lightColor;

void main(){
    outColor = vec4(lightColor * objectColor, 1.0);
}