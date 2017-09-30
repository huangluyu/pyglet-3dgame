import BasicEntity as BE


class Scene:
    # main_world = None
    #
    # def __init__(self):
    #     self.main_world = world

    @staticmethod
    def load_cube_3x4():
        # 设置场景方块
        cube_list = [
            BE.Cube(BE.Point(0, 200, 200), 200),
            BE.Cube(BE.Point(0, 200, 400), 200),
            BE.Cube(BE.Point(0, 200, 600), 200), 
            BE.Cube(BE.Point(0, 200, 800), 200), 
            BE.Cube(BE.Point(0, 400, 200), 200), 
            BE.Cube(BE.Point(0, 400, 400), 200), 
            BE.Cube(BE.Point(0, 400, 600), 200), 
            BE.Cube(BE.Point(0, 400, 800), 200), 
            BE.Cube(BE.Point(0, 600, 200), 200), 
            BE.Cube(BE.Point(0, 600, 400), 200), 
            BE.Cube(BE.Point(0, 600, 600), 200), 
            BE.Cube(BE.Point(0, 600, 800), 200)
        ]
        return cube_list