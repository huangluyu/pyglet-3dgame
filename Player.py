import BasicEntity

class Player:
    location = None
    faceTo = None
    dpi = 100
    player = None

    def __init__(self, location, faceTo):
        self.location = location
        self.faceTo = faceTo

    def face_up(self, change):
        self.faceTo.angle_z += change * self.dpi / 150
        if self.faceTo.angle_z > 180:
            self.faceTo.angle_z = 180
        elif self.faceTo.angle_z < 0:
            self.faceTo.angle_z = 0

    def face_left(self, change):
        self.faceTo.angle_x += change * self.dpi / 150
        if self.faceTo.angle_x > 360:
            self.faceTo.angle_x -= 360
        elif self.faceTo.angle_x < 0:
            self.faceTo.angle_x += 360

    def __str__(self):
        return '人物的坐标为:%.3f, %.3f, %.3f, 面朝:正向%.3f度, 垂直%.3f度' % (
            self.location.x, self.location.y, self.location.z, self.faceTo.angle_x, self.faceTo.angle_z
        )