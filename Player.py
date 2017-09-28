import BasicEntity


class Player:
    location = None
    face_to = None
    player = None
    personal_set = None
    speed = dict(w = False, s = False, a = False, d = False, shift = False, space = False, c = False)

    def __init__(self, location, face_to):
        self.location = location
        self.face_to = face_to
        self.personal_set = Set()

    def face_up(self, change):
        self.face_to.angle_z += change * self.personal_set.dpi / 200
        if self.face_to.angle_z > 180:
            self.face_to.angle_z = 180
        elif self.face_to.angle_z < 0:
            self.face_to.angle_z = 0
        self.face_to.turn_descartes()

    def face_left(self, change):
        self.face_to.angle_x += change * self.personal_set.dpi / 200
        if self.face_to.angle_x > 360:
            self.face_to.angle_x -= 360
        elif self.face_to.angle_x < 0:
            self.face_to.angle_x += 360
        self.face_to.turn_descartes()

    def move(self, dt):
        move_to = BasicEntity.Point(0, 0, 0)
        if self.speed["w"]:
            move_to += self.face_to * -1
        if self.speed["s"]:
            move_to += self.face_to
        if self.speed["d"]:
            move_to += BasicEntity.Point(-self.face_to.y, self.face_to.x, 0).to_modulo_one() * 100
        if self.speed["a"]:
            move_to += BasicEntity.Point(self.face_to.y, -self.face_to.x, 0).to_modulo_one() * 100
        if self.speed['space']:
            move_to += BasicEntity.Point(0, 0, -1).to_modulo_one() * 100
        if self.speed['c']:
            move_to += BasicEntity.Point(0, 0, 1).to_modulo_one() * 100
        if self.speed['shift']:
            move_to *= 3
        self.location -= move_to * dt
        self.location.turn_sphere()

    def __str__(self):
        return '人物的坐标为:%.3f, %.3f, %.3f, 面朝:正向%.3f度, 垂直%.3f度' % (
            self.location.x, self.location.y, self.location.z, self.face_to.angle_x, self.face_to.angle_z
        )


class Set:
    dpi = 100
    visual_range = 1000
    screen_range = 50
    screen_width = 1000
    screen_height = 800
