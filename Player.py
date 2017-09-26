import BasicEntity


class Player:
    location = None
    face_to = None
    player = None
    personal_set = None

    def __init__(self, location, face_to):
        self.location = location
        self.face_to = face_to
        self.personal_set = Set()

    def face_up(self, change):
        self.face_to.angle_z += change * self.personal_set.dpi / 1000
        if self.face_to.angle_z > 180:
            self.face_to.angle_z = 180
        elif self.face_to.angle_z < 0:
            self.face_to.angle_z = 0
        self.face_to.turn_descartes()

    def face_left(self, change):
        self.face_to.angle_x += change * self.personal_set.dpi / 1000
        if self.face_to.angle_x > 360:
            self.face_to.angle_x -= 360
        elif self.face_to.angle_x < 0:
            self.face_to.angle_x += 360
        self.face_to.turn_descartes()

    def __str__(self):
        return '人物的坐标为:%.3f, %.3f, %.3f, 面朝:正向%.3f度, 垂直%.3f度' % (
            self.location.x, self.location.y, self.location.z, self.face_to.angle_x, self.face_to.angle_z
        )


class Set:
    dpi = 100
    visual_range = 1000
    screen_width = 1000
    screen_height = 800
