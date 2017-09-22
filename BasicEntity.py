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
        if self.r > 0:
            self.angle_z = math.acos(self.z / self.r) * 180 / math.pi
            if not (self.x == 0 and self.y == 0):
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


# 实体
class BasicEntity:
    point_list = []
    link_list = [[]]


# 方块
class Cube(BasicEntity):
    # pointA1 = None
    # pointA2 = None
    # pointA3 = None
    # pointA4 = None
    # pointB1 = None
    # pointB2 = None
    # pointB3 = None
    # pointB4 = None
    point_list = []


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


# 平面
class Plane:
    # 平面方程 Ax + By + Cz + D = 0
    a = 0
    b = 0
    c = 0
    d = 0

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def check_point(self, point):
        answer = self.a * point.x + self.b * point.y + self.c * point.z + self.d
        if round(answer, 3) == 0:
            return 0
        elif answer < 0:
            return -1
        else:
            return 1