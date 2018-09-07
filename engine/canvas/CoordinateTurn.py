import math


# 角度转换处理类
class CoordinateRotate:

    # x轴旋转
    @staticmethod
    def __rotate_x(x, y, z, angle):
        x = x
        y = y * math.cos(angle) - z * math.sin(angle)
        z = y * math.sin(angle) + z * math.cos(angle)
        return x, y, z

    # y轴旋转
    @staticmethod
    def __rotate_y(x, y, z, angle):
        x = x * math.sin(angle) + z * math.cos(angle)
        y = y
        z = z * math.cos(angle) - x * math.sin(angle)
        return x, y, z

    # z轴旋转
    @staticmethod
    def __rotate_z(x, y, z, angle):
        x = x * math.cos(angle) - y * math.sin(angle)
        y = x * math.sin(angle) + y * math.cos(angle)
        z = z
        return x, y, z

    # 三项旋转 （三个角度依次旋转）
    @staticmethod
    def rotate(self, point, angle_x, angle_y, angle_z):
        x, y, z = point.get_xyz()
        return self.__rotate_z(self.__rotate_y(self.__rotate_x(x, y, z, angle_x), angle_y), angle_z)
