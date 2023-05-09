#version 330

in vec3 pos;
in vec2 in_tex;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 tex;

void main() {
    gl_Position = projection * view * model * vec4(pos, 1.0);
    tex = in_tex;
}
