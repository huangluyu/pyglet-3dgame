from abc import abstractmethod

from engine.entity.base import StaticEntity
from engine.entity.base.BasicEntity import BasicEntity


class DynamicEntity(BasicEntity):
    # 速度
    speed = 10
    # 坐标
    location = None
    # 面部朝向
    face_to = None
    # 存储数据
    info = dict()

    @abstractmethod
    def update(self, dt):
        pass

    # 初始化设置位置及面朝方向
    def __init__(self, location, face_to):
        self.location = location
        self.face_to = face_to


class MoveCube(DynamicEntity):

    # 初始化设置位置及面朝方向
    def __init__(self, location, face_to):
        cube = StaticEntity.Cube(location, 100)
        self.point_list = cube.point_list
        self.link_list = cube.link_list
        self.info["start_location"] = location
        self.info["start_face"] = face_to
        self.info["target"] = True
        super().__init__(location, face_to)

    def update(self, dt):
        self.location += self.face_to * dt * 50
        for point in self.point_list:
            point << point + self.face_to * dt * 50
        print(self.face_to)
        if self.location.x - self.info["start_location"].x > 10 * self.face_to.x and self.info["target"]:
            self.info["target"] = False
            for point in self.point_list:
                point << point - (self.location - self.info["start_location"] - self.face_to * 10)
            self.location = self.info["start_location"] + self.face_to * 10
            print("1111", self.face_to)
            self.face_to << self.face_to * -1
            print(self.face_to)
        elif self.location.x - self.info["start_location"].x < 10 * self.face_to.x and not self.info["target"]:
            self.info["target"] = True
            for point in self.point_list:
                point << point - (self.location - self.info["start_location"] - self.face_to * 10)
            self.location = self.info["start_location"] + self.face_to * 10
            print("2222", self.face_to)
            self.face_to << self.face_to * -1
            print(self.face_to)
