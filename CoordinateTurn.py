import math


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
