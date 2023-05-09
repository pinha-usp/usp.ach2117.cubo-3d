import glm
import pathlib
import numpy as np
from cube import Cube
import moderngl as mgl
import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO

class Window(mglw.WindowConfig):

    gl_version = (3, 3)
    title = "Cube"
    window_size = (800, 600)
    resource_dir = pathlib.Path("resources")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.program = self.load_program(
            vertex_shader = "shaders/default.vert",
            fragment_shader = "shaders/default.frag",
        )

        cube = Cube()

        self.texture = self.load_texture_2d("textures/box.jpg")

        self.vao = VAO(mode = mgl.TRIANGLES)
        self.vao.buffer(
            buffer = cube.vertices.tobytes(),
            buffer_format = "3f",
            attribute_names = ["pos"]
        )
        self.vao.buffer(
            buffer = cube.textures.tobytes(),
            buffer_format = "2f",
            attribute_names = ["in_tex"]
        )
        self.vao.index_buffer(cube.faces.tobytes())

        self.projection = glm.perspective(
            glm.radians(45.0),
            self.wnd.width / self.wnd.height,
            0.1,
            100.0
        )

    def render(self, time, frametime):
        self.ctx.enable(mgl.DEPTH_TEST)

        self.model = glm.translate(
            glm.mat4(1.0),
            glm.vec3(0.0, 0.0, -2.0)
        )

        self.model = glm.rotate(
            self.model,
            glm.radians(-25.0 + time * 50),
            glm.vec3(1.0, 1.0, 0.0)
        )

        self.view = glm.translate(
            glm.mat4(1.0),
            glm.vec3(0.0, 0.0, 1.0)
        )

        self.program["model"].write(self.model)
        self.program["view"].write(self.view)
        self.program["projection"].write(self.projection)

        self.texture.use()

        self.vao.render(self.program)
