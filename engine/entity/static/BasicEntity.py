from engine.entity.base.BasicEntity import Point
from engine.entity.base.StaticEntity import StaticEntity


class Square(StaticEntity):

    def __init__(self, center, length):
        self.point_list = [
            Point(center.x - length / 2, center.y - length / 2, center.z + length / 2),
            Point(center.x + length / 2, center.y - length / 2, center.z + length / 2),
            Point(center.x - length / 2, center.y - length / 2, center.z - length / 2),
            Point(center.x + length / 2, center.y - length / 2, center.z - length / 2)
        ]
        self.link_list = [
            [0, 1], [1, 2], [2, 3], [3, 0]
        ]


class Cube(StaticEntity):

    def __init__(self, center, length):
        self.point_list = self.__cube_point_list(center, length)
        self.link_list = [
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]
        ]

    @staticmethod
    def __cube_point_list(center, length):
        return [
            Point(center.x + length / 2, center.y + length / 2, center.z + length / 2),
            Point(center.x - length / 2, center.y + length / 2, center.z + length / 2),
            Point(center.x - length / 2, center.y - length / 2, center.z + length / 2),
            Point(center.x + length / 2, center.y - length / 2, center.z + length / 2),
            Point(center.x + length / 2, center.y + length / 2, center.z - length / 2),
            Point(center.x - length / 2, center.y + length / 2, center.z - length / 2),
            Point(center.x - length / 2, center.y - length / 2, center.z - length / 2),
            Point(center.x + length / 2, center.y - length / 2, center.z - length / 2)
        ]
