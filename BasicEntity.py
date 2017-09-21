import math


class Point:
    x = 0
    y = 0
    z = 0
    r = 0
    angle_x = 0
    angle_z = 0

    def __init__(self, x, y, z, r = 0, angle_x = 0, angle_z = 0):
        if r == 0 :
            self.x = x
            self.y = y
            self.z = z
            self.turn_sphere()
        else:
            self.r = r
            self.angle_x = angle_x
            self.angle_z = angle_z
            self.turn_descartes()

    def get_xyz(self):
        return self.x, self.y, self.z

    def turn_descartes(self):
        l = math.sin(self.angle_z * math.pi / 180) * self.r
        self.x = l * math.cos(self.angle_x * math.pi / 180)
        self.y = l * math.sin(self.angle_x * math.pi / 180)
        self.z = math.cos(self.angle_z * math.pi / 180) * self.r

    def turn_sphere(self):
        self.r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.angle_z = math.acos(self.z / self.r) * 180 / math.pi
        self.angle_x = math.acos(self.x / math.sqrt(self.x ** 2 + self.y ** 2)) * 180 / math.pi

    def __str__(self):
        return '点的坐标为: %.3f, %.3f, %.3f 长度为%.3f 横轴%.3f度 纵轴%.3f度' % (
            self.x, self.y, self.z, self.r, self.angle_x, self.angle_z
        )


# 球坐标系向量
class Vector:
    x = 0
    y = 0
    z = 0

    def __init__(self, r, angle_x, angle_z):
        # self.reset(r, angle_x, angle_z)
        self.r = r
        self.angle_x = angle_x
        self.angle_z = angle_z

    def reset(self, x, y, z):
        k = math.sqrt(x ** 2 + y ** 2 + z ** 2)
        self.xV = round(x / k , 2)
        self.yV = round(y / k , 2)
        self.zV = round(z / k , 2)


class Cube:
    # pointA1 = None
    # pointA2 = None
    # pointA3 = None
    # pointA4 = None
    # pointB1 = None
    # pointB2 = None
    # pointB3 = None
    # pointB4 = None
    pointList = [None, None, None, None, None, None, None, None]
    link = [[1, 2], [2, 3], [3, 4], [4, 1],
            [5, 6], [6, 7], [7, 8], [8, 5],
            [1, 5], [2, 6], [3, 7], [4, 8]]

    def __init__(self, center, length):
        self.point_list = self.__point_list(center, length)

    def __point_list(self, center, length):
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

