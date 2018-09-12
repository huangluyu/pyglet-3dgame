import math

from engine.config import Set


# 平面点
class CanvasPoint:
    # x轴坐标
    x = 0
    # y轴坐标
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 判断点是否在屏幕外面（超出画布面视野范围）
    def is_out_screen(self):
        return self.x < 0 or self.x > Set.screen_width or self.y < 0 or self.y >= Set.screen_height

    # 重写 + 变为两点坐标相加
    def __add__(self, point):
        return CanvasPoint(self.x + point.x, self.y + point.y)


# 点 或者 向量
class Point(CanvasPoint):
    # z轴坐标
    z = 0

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # 获得坐标轴的值
    def get_xyz(self):
        return self.x, self.y, self.z

    # # 翻转？转身?
    # def reverse(self):
    #     self.x *= -1
    #     self.y *= -1
    #     self.z *= -1
    #     self.turn_sphere()
    #     return self

    # 重写 * 变为求两向量点积
    def __mul__(self, target):
        if type(target) == int or type(target) == float:
            return Point(self.x * target, self.y * target, self.z * target)

    # 重写 + 变为两点坐标相加
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    # 重写 - 变为两点坐标相减
    def __sub__(self, point):
        return Vector(self.x - point.x, self.y - point.y, self.z - point.z)

    # 输出点的坐标
    def __str__(self):
        return '点的坐标为: %.3f, %.3f, %.3f' % (
            self.x, self.y, self.z
        )

    def __repr__(self):
        return self.__str__()


class Vector(Point):
    # 球坐标系r
    r = 0
    # 球坐标系x旋转角
    angle_x = 0
    # 球坐标系z旋转角
    angle_z = 0

    def __init__(self, x, y, z, r=0, angle_x=0, angle_z=0):
        super().__init__(x, y, z)
        if r == 0:
            self.x = x
            self.y = y
            self.z = z
            self.turn_sphere()
        else:
            self.r = r
            self.angle_x = angle_x
            self.angle_z = angle_z
            self.turn_descartes()

    # 将球坐标系的数值同步到直角坐标系上
    def turn_descartes(self):
        ln = math.sin(self.angle_z * math.pi / 180) * self.r
        self.x = round(ln * math.cos(self.angle_x * math.pi / 180), 3)
        self.y = round(ln * math.sin(self.angle_x * math.pi / 180), 3)
        self.z = round(math.cos(self.angle_z * math.pi / 180) * self.r, 3)

    # 将直角坐标系的值同步到球坐标系上
    def turn_sphere(self):
        self.r = math.sqrt(self.modulo_fang())
        if self.r > 0:
            self.angle_z = math.acos(self.z / self.r) * 180 / math.pi
            if not (self.x == 0 and self.y == 0):
                self.angle_x = math.acos(self.x / math.sqrt(self.x ** 2 + self.y ** 2)) * 180 / math.pi

    # 获得x,y,z的模的平方和
    def modulo_fang(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    # 将向量长度缩放到模为1
    def to_modulo_one(self):
        module = math.sqrt(self.modulo_fang())
        if module > 0:
            self.x /= module
            self.y /= module
            self.z /= module
            self.turn_sphere()
        return self

    # 输出点的坐标
    def __str__(self):
        return '点的坐标为: %.3f, %.3f, %.3f 长度为%.3f 横轴%.3f度 纵轴%.3f度' % (
            self.x, self.y, self.z, self.r, self.angle_x, self.angle_z
        )

    # 重写 * 变为求两向量点积
    def __mul__(self, target):
        if type(target) == Vector:
            return self.x * target.x + self.y * target.y + self.z * target.z
        elif type(target) == int or type(target) == float:
            return Vector(self.x * target, self.y * target, self.z * target)

    # 重写 + 变为两点坐标相加
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    # 重写 - 变为两点坐标相减
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)


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

    # 验证点是否在平面上
    def check_point(self, point):
        answer = self.a * point.x + self.b * point.y + self.c * point.z + self.d
        if round(answer, 3) == 0:
            return 0
        elif answer < 0:
            return -1
        else:
            return 1
