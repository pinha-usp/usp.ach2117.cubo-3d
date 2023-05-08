import glm
import pathlib
import numpy as np
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

        self.vertices = np.array([
            [-0.5, 0.8, 0.0],
            [0.5, 0.8, 0.0],
            [0.5, -0.8, 0.0],
            [-0.5, -0.8, 0.0]
        ], dtype=np.float32)

        self.vao = VAO(mode = mgl.TRIANGLE_FAN)
        self.vao.buffer(
            buffer = self.vertices.tobytes(),
            buffer_format = "3f",
            attribute_names = ["pos"]
        )

        self.projection = glm.perspective(
            glm.radians(45.0),
            self.wnd.width / self.wnd.height,
            0.1,
            100.0
        )

    def render(self, time, frametime):
        self.ctx.clear()

        self.model = glm.translate(
            glm.mat4(1.0),
            glm.vec3(0.0, 0.0, -10.0)
        )

        self.model = glm.rotate(
            self.model,
            glm.radians(-55.0 + time * 100),
            glm.vec3(1.0, 0.0, 0.0)
        )

        self.view = glm.translate(
            glm.mat4(1.0),
            glm.vec3(0.0, 0.0, 1.0 * time)
        )

        self.program["model"].write(self.model)
        self.program["view"].write(self.view)
        self.program["projection"].write(self.projection)

        self.vao.render(self.program)
