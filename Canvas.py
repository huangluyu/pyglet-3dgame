import pyglet, math, time
import Player, BasicEntity as BE, World


class Canvas:
    angle = 0
    world = None
    window = None
    plane = None

    def __init__(self, world):
        self.world = world
        personal_set = world.player.personal_set
        self.window = pyglet.window.Window(personal_set.screen_width, personal_set.screen_height)
        # self.window.set_exclusive_mouse(True)

    @staticmethod
    def draw_line(a, b, ta, tb):
        pyglet.graphics.draw(
            2,
            pyglet.gl.GL_LINES,
            ('v2f', (a, b, ta, tb)),
            ('c3B', (255, 255, 255, 255, 255, 255))
        )

    def draw_square(self, radius, angle, k):
        angle *= 2 * math.pi / 360
        pointZeroX = self.world.player.personal_set.screen_width // 2
        pointZeroY = self.world.player.personal_set.screen_height // 2
        x1 = pointZeroX + radius * math.cos(angle)
        y1 = pointZeroY + radius * math.sin(angle) * k
        x2 = pointZeroX + radius * math.sin(angle)
        y2 = pointZeroY - radius * math.cos(angle) * k
        x3 = pointZeroX - radius * math.cos(angle)
        y3 = pointZeroY - radius * math.sin(angle) * k
        x4 = pointZeroX - radius * math.sin(angle)
        y4 = pointZeroY + radius * math.cos(angle) * k
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x4, y4)
        self.draw_line(x4, y4, x1, y1)

    def change_angle(self, dt):
        radius = 200
        self.angle = self.angle + dt * 50
        k = 1
        if self.angle >= 360:
            self.angle = 0
        self.draw_square(radius, self.angle, k)

    def canvas_plane(self):
        player = self.world.player
        d = -(
            player.face_to.x * player.location.x
            + player.face_to.y * player.location.y
            + player.face_to.z * player.location.y
            + math.sqrt(player.face_to.modulo_fang())
        )
        return BE.Plane(player.face_to.x, player.face_to.y, player.face_to.z, d)

    def canvas_plane_cross_point(self, target_point):
        player = self.world.player
        mol = player.face_to.modulo_fang()
        a = player.face_to.x * (target_point.x - player.location.x) \
            + player.face_to.y * (target_point.y - player.location.y) \
            + player.face_to.z * (target_point.z - player.location.z)
        k = mol / a if a != 0 else 0
        plane_x = k * (target_point.x - player.location.x) + player.location.x
        plane_y = k * (target_point.y - player.location.y) + player.location.y
        plane_z = k * (target_point.z - player.location.z) + player.location.z
        return BE.Point(plane_x, plane_y, plane_z)

    @staticmethod
    def space_to_canvas(space_point, x_vector, y_vector, canvas_zero):
        vector = space_point - canvas_zero
        x = vector * x_vector
        y = vector * y_vector
        return BE.Point(x, y, 0)

    def get_new_xy_vector(self):
        player = self.world.player
        canvas_zero = player.location + player.face_to
        x_vector = BE.Point(
            player.face_to.y,
            - player.face_to.x,
            0
        ).to_modulo_one()
        y_vector = BE.Point(
            - player.face_to.z * player.face_to.x,
            - player.face_to.z * player.face_to.y,
            player.face_to.y ** 2 + player.face_to.x ** 2
        ).to_modulo_one()
        # y>0时x轴正方向为x增大方向
        # if ((math.cos(player.face_to.angle_x) > 0 and x_vector.x < 0)
        #     or (math.cos(player.face_to.angle_x) < 0 and x_vector.x > 0)):
        #     x_vector.reverse()
        # if y_vector.z < 0:
        #     y_vector.reverse()
        return x_vector, y_vector, canvas_zero

    def is_visible(self, point):
        player = self.world.player
        A = player.face_to.x
        B = player.face_to.y
        C = player.face_to.z
        return A * point.x + B * point.y + C * point.z \
               > player.location.x * A + player.location.y * B + player.location.z * C

    def tick_draw(self, dt):
        self.plane = self.canvas_plane()
        x_vector, y_vector, canvas_zero = self.get_new_xy_vector()
        canvas_point_list = []
        canvas_point_visible = []
        self.world.player.move(dt)
        for point in self.world.point_list:
            space_point = self.canvas_plane_cross_point(point)
            canvas_point = self.space_to_canvas(space_point, x_vector, y_vector, canvas_zero)
            screen_reset = BE.Point(
                self.world.player.personal_set.screen_width / 2,
                self.world.player.personal_set.screen_height / 2,
                0
            )
            canvas_point_list.append(canvas_point + screen_reset)
            canvas_point_visible.append(self.is_visible(point))
        self.window.clear()
        for line in self.world.line_list:
            if (canvas_point_visible[line[0]] and canvas_point_visible[line[1]]):
                Canvas.draw_line(
                    canvas_point_list[line[0]].x, canvas_point_list[line[0]].y,
                    canvas_point_list[line[1]].x, canvas_point_list[line[1]].y
                )
            # elif (canvas_point_visible[line[0]]):
            #     self.world.point_list[]
            #     Canvas.draw_line(canvas_point_list[line[0]].x, canvas_point_list[line[0]].y, canvas_point_list[line[1]].x, canvas_point_list[line[1]].y)
            # elif (canvas_point_visible[line[1]]):
            #     Canvas.draw_line(canvas_point_list[line[0]].x, canvas_point_list[line[0]].y, canvas_point_list[line[1]].x, canvas_point_list[line[1]].y)


# label = pyglet.text.Label('去你妈的祖国的花朵',
#                           font_name = 'Times New Roman',
#                           font_size = 36,
#                           x = window.width//2, y = window.height//2,
#                           anchor_x = 'center', anchor_y = 'center')
# player_ship = pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
#                          ('v2i', (10, 15, 30, 35)),
#                          ('c3B', (0, 0, 255, 0, 255, 0))
#                          )


world = World.World(Player.Player(BE.Point(0, 0, 100), BE.Point(0, 0, 0, 100, 0, 90)))
canvas = Canvas(world)
main_window = canvas.window
key = pyglet.window.key


@main_window.event
def on_draw():
    radius = 100


@main_window.event()
def on_mouse_motion(x, y, dx, dy):
    global world
    player = world.player
    player.face_up(-dy)
    player.face_left(-dx)


@main_window.event()
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        world.player.speed['w'] = True
        world.player.speed['s'] = False
    elif symbol == key.S:
        world.player.speed['w'] = False
        world.player.speed['s'] = True
    elif symbol == key.A:
        world.player.speed['d'] = False
        world.player.speed['a'] = True
    elif symbol == key.D:
        world.player.speed['a'] = False
        world.player.speed['d'] = True


@main_window.event()
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        world.player.speed['w'] = False
    elif symbol == key.S:
        world.player.speed['s'] = False
    elif symbol == key.A:
        world.player.speed['a'] = False
    elif symbol == key.D:
        world.player.speed['d'] = False


world.put(BE.Cube(BE.Point(0, 200, 200), 200))
world.put(BE.Cube(BE.Point(0, 200, 400), 200))
world.put(BE.Cube(BE.Point(0, 200, 600), 200))
world.put(BE.Cube(BE.Point(0, 200, 800), 200))
world.put(BE.Cube(BE.Point(0, 400, 200), 200))
world.put(BE.Cube(BE.Point(0, 400, 400), 200))
world.put(BE.Cube(BE.Point(0, 400, 600), 200))
world.put(BE.Cube(BE.Point(0, 400, 800), 200))
world.put(BE.Cube(BE.Point(0, 600, 200), 200))
world.put(BE.Cube(BE.Point(0, 600, 400), 200))
world.put(BE.Cube(BE.Point(0, 600, 600), 200))
world.put(BE.Cube(BE.Point(0, 600, 800), 200))
# world.put(BE.Cube(BE.Point(200, 200, 100), 200))
pyglet.clock.schedule_interval(canvas.tick_draw, 1/60)
pyglet.app.run()
