import math, BasicEntity


class World:
    point_list = []
    line_list = []

    def add_static_entity(self, static_entity):
        length = len(self.point_list)
        for e_link in static_entity.link_list:
            link = [e_link[0] + length, e_link[1] + length]
            print(link)
            self.line_list.append(link)
        print(self.line_list)
        for e_point in static_entity.point_list:
            self.point_list.append(e_point)

    def put(self, entity):
        if isinstance(entity, BasicEntity.BasicEntity):
            self.add_static_entity(entity)

