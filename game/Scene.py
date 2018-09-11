from engine.entity.static import StaticBasicEntity as StaticBasicEntity
from engine.entity.base import BasicEntity


class Scene:

    @staticmethod
    def load_cube_3x4():
        # 设置场景方块
        cube_list = [
            StaticBasicEntity.Cube(BasicEntity.Point(0, 200, 200), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 200, 400), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 200, 600), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 200, 800), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 400, 200), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 400, 400), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 400, 600), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 400, 800), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 600, 200), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 600, 400), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 600, 600), 200),
            StaticBasicEntity.Cube(BasicEntity.Point(0, 600, 800), 100),
        ]
        return cube_list

    @staticmethod
    def load_line():
        a = BasicEntity.BasicEntity()
        a.link_list = [[0, 1]]
        a.point_list = [
            BasicEntity.Point(1, 100, 0),
            BasicEntity.Point(-100, -100, 0)
        ]
        return [
            a
        ]

    @staticmethod
    def load_square():
        return [
            StaticBasicEntity.Square(BasicEntity.Point(0, 0, 0), 200)
        ]