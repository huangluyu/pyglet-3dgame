from engine.entity.base import Space
from engine.entity.base import BasicEntity, StaticEntity


class Scene:

    @staticmethod
    def load_cube_3x4():
        # 设置场景方块
        cube_list = [
            StaticEntity.Cube(Space.Point(0, 200, 200), 200),
            StaticEntity.Cube(Space.Point(0, 200, 400), 200),
            StaticEntity.Cube(Space.Point(0, 200, 600), 200),
            StaticEntity.Cube(Space.Point(0, 200, 800), 200),
            StaticEntity.Cube(Space.Point(0, 400, 200), 200),
            StaticEntity.Cube(Space.Point(0, 400, 400), 200),
            StaticEntity.Cube(Space.Point(0, 400, 600), 200),
            StaticEntity.Cube(Space.Point(0, 400, 800), 200),
            StaticEntity.Cube(Space.Point(0, 600, 200), 200),
            StaticEntity.Cube(Space.Point(0, 600, 400), 200),
            StaticEntity.Cube(Space.Point(0, 600, 600), 200),
            StaticEntity.Cube(Space.Point(0, 600, 800), 200),
        ]
        return cube_list

    @staticmethod
    def load_line():
        a = BasicEntity.BasicEntity()
        a.link_list = [[0, 1], [0, 2]]
        a.point_list = [
            Space.Point(100, 0, 0),
            Space.Point(-100, -100, 200),
            Space.Point(-100, -100, 100)
        ]
        return [
            a
        ]

    @staticmethod
    def load_square():
        return [
            StaticEntity.Square(Space.Point(0, 0, 0), 200)
        ]