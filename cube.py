import numpy as np

class Cube:

    def __init__(self):
        self.vertices = np.array([
            -0.2, -0.2, -0.2,
            -0.2, -0.2,  0.2,
            -0.2,  0.2, -0.2,
            -0.2,  0.2,  0.2,
             0.2, -0.2, -0.2,
             0.2, -0.2,  0.2,
             0.2,  0.2, -0.2,
             0.2,  0.2,  0.2
        ], dtype = np.float32)

        self.faces = np.array([
            0, 1, 2,
            1, 3, 2,
            4, 5, 6,
            5, 7, 6,
            0, 4, 1,
            4, 5, 1,
            1, 5, 3,
            5, 7, 3,
            0, 2, 4,
            2, 6, 4,
            2, 3, 6,
            3, 7, 6
        ], dtype = np.int32)

        self.textures = np.array([
            0.0, 0.0,
            0.0, 1.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 0.0,
            0.0, 1.0,
            1.0, 0.0,
            1.0, 1.0
        ], dtype=np.float32)

