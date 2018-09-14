from engine.entity.base.DynamicEntity import DynamicEntity
from engine.entity.base.StaticEntity import StaticEntity


class World:
    # 玩家
    player = None
    # 点列表
    point_list = []
    # 线列表
    line_list = []
    # 动态实体列表
    dynamic_list = []

    # 初始化设置玩家
    def __init__(self, player):
        World.player = player

    # 新增静态实体
    def add_static_entity(self, static_entity):
        length = len(self.point_list)
        for e_link in static_entity.link_list:
            link = [e_link[0] + length, e_link[1] + length]
            self.line_list.append(link)
        for e_point in static_entity.point_list:
            self.point_list.append(e_point)

    # 新增动态实体
    def add_dynamic_entity(self, dynamic_entity):
        self.dynamic_list.append(dynamic_entity)
        self.add_static_entity(dynamic_entity)

    # 新增实体
    def put(self, entity):
        if isinstance(entity, StaticEntity):
            self.add_static_entity(entity)
        elif isinstance(entity, DynamicEntity):
            self.add_dynamic_entity(entity)
        elif isinstance(entity, list):
            for singleEntity in entity:
                self.add_static_entity(singleEntity)

    def update(self, dt):
        for dynamic in self.dynamic_list:
            dynamic.update(dt)

    # 判断是否可见
    def charge_visible(self):
        square_range = {
            'x_min': self.player.x - self.player.personal_set.visual_range,
            'x_max': self.player.x + self.player.personal_set.visual_range,
            'y_min': self.player.y - self.player.personal_set.visual_range,
            'y_max': self.player.y - self.player.personal_set.visual_range
        }
        # 看得见的点
        visible_point = []
        # 简单正方形判断
        for num, point in enumerate(self.point_list):
            if square_range['x_max'] >= point.x >= square_range['x_min'] and square_range['y_max'] >= point.y >= \
                    square_range['y_min']:
                visible_point.append(num)
