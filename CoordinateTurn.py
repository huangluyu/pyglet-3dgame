import math


class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_xyz(self):
        return self.x, self.y, self.z


class Vector:
    xV = 0
    yV = 0
    zV = 0

    def __init__(self, xV, yV, zV):
        self.xV = xV
        self.yV = yV
        self.zV = zV


class Cube:
    # pointA1 = None
    # pointA2 = None
    # pointA3 = None
    # pointA4 = None
    # pointB1 = None
    # pointB2 = None
    # pointB3 = None
    # pointB4 = None
    # pointList = [None, None, None, None, None, None, None, None]

    def __init__(self, point_list):
        self.point_list = point_list


class CoordinateRotate:

    @staticmethod
    def __rotate_x(self, x, y, z, angle):
        x = x
        y = y * math.cos(angle) - z * math.sin(angle)
        z = y * math.sin(angle) + z * math.cos(angle)
        return x, y, z

    @staticmethod
    def __rotate_y(self, x, y, z, angle):
        x = x * math.sin(angle) + z * math.cos(angle)
        y = y
        z = z * math.cos(angle) - x * math.sin(angle)
        return x, y, z

    @staticmethod
    def __rotate_z(self, x, y, z, angle):
        x = x * math.cos(angle) - y * math.sin(angle)
        y = x * math.sin(angle) + y * math.cos(angle)
        z = z
        return x, y, z

    @staticmethod
    def rotate(self, point, angle_x, angle_y, angle_z):
        x,y,z = point.get_xyz()
        return self.__rotate_z(self.__rotate_y(self.__rotate_x(x, y, z, angle_x), angle_y), angle_z)
