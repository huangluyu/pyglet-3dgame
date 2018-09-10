from engine.config import Set
from engine.entity.base.DynamicEntity import DynamicEntity


class Player(DynamicEntity):
    # 玩家坐标
    location = None
    # 玩家面部朝向
    face_to = None

    # 初始化设置位置及面朝方向
    def __init__(self, location, face_to):
        self.location = location
        self.face_to = face_to

    # 抬头
    def face_up(self, change):
        self.face_to.angle_z += change * Set.dpi / 200
        if self.face_to.angle_z >= 180:
            self.face_to.angle_z = 179.99
        elif self.face_to.angle_z <= 0:
            self.face_to.angle_z = 0.01
        self.face_to.turn_descartes()

    # 左右转头
    def face_left(self, change):
        self.face_to.angle_x += change * Set.dpi / 200
        if self.face_to.angle_x > 360:
            self.face_to.angle_x -= 360
        elif self.face_to.angle_x < 0:
            self.face_to.angle_x += 360
        self.face_to.turn_descartes()

    # 位置移动
    def move(self, move_to):
        self.location -= move_to
        # TODO 会发生什么？
        # self.location.turn_sphere()

    # 打印人物信息
    def __str__(self):
        return '人物的坐标为:%.3f, %.3f, %.3f, 面朝:正向%.3f度, 垂直%.3f度' % (
            self.location.x, self.location.y, self.location.z, self.face_to.angle_x, self.face_to.angle_z
        )

    def __repo__(self):
        return self.__str__()
