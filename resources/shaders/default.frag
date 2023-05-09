#version 330

in vec2 tex; 

uniform sampler2D texture0;

void main() {
    gl_FragColor = texture(texture0, tex);
}
