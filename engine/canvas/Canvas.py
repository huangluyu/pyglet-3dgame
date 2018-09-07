import math
import pyglet

import engine.entity.base.BasicEntity
import engine.entity.base.StaticEntity

# 画布类
from engine.config import Set
from engine.control.InputControl import InputControl
from engine.entity.World import World


class Canvas:
    # ？角度
    angle = 0
    # 当前世界
    world = None
    # 当前 pyglet 窗口
    window = None
    # 画布平面
    plane = None
    # 时刻
    dt = 1 / 200

    def __init__(self, world, window):
        self.world = world
        # self.window = pyglet.window.Window(personal_set.screen_width, personal_set.screen_height)
        self.window = window
        # self.window.set_exclusive_mouse(True)

    # 画一条线
    @staticmethod
    def draw_line(a, b, ta, tb):
        pyglet.graphics.draw(
            2,
            pyglet.gl.GL_LINES,
            ('v2f', (a, b, ta, tb)),
            ('c3B', (255, 255, 255, 255, 255, 255))
        )

    # 画一个正方形
    def draw_square(self, radius, angle, k):
        angle *= 2 * math.pi / 360
        point_zero_x = Set.screen_width // 2
        point_zero_y = Set.screen_height // 2
        x1 = point_zero_x + radius * math.cos(angle)
        y1 = point_zero_y + radius * math.sin(angle) * k
        x2 = point_zero_x + radius * math.sin(angle)
        y2 = point_zero_y - radius * math.cos(angle) * k
        x3 = point_zero_x - radius * math.cos(angle)
        y3 = point_zero_y - radius * math.sin(angle) * k
        x4 = point_zero_x - radius * math.sin(angle)
        y4 = point_zero_y + radius * math.cos(angle) * k
        self.draw_line(x1, y1, x2, y2)
        self.draw_line(x2, y2, x3, y3)
        self.draw_line(x3, y3, x4, y4)
        self.draw_line(x4, y4, x1, y1)

    # 改变角度 ???
    def change_angle(self, dt):
        radius = 200
        self.angle = self.angle + dt * 50
        k = 1
        if self.angle >= 360:
            self.angle = 0
        self.draw_square(radius, self.angle, k)

    # 计算画布平面在世界坐标系中的平面(实时绘制)
    def canvas_plane(self):
        player = self.world.player
        d = -(
                player.face_to.x * player.location.x
                + player.face_to.y * player.location.y
                + player.face_to.z * player.location.y
                + math.sqrt(player.face_to.modulo_fang())
        )
        return engine.entity.base.BasicEntity.Plane(player.face_to.x, player.face_to.y, player.face_to.z, d)

    # 计算点在画布上的投影点（世界坐标系）
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
        return engine.entity.base.BasicEntity.Point(plane_x, plane_y, plane_z)

    #
    def space_to_canvas(self, space_point, x_vector, y_vector, canvas_zero):
        vector = space_point - canvas_zero
        x = vector * x_vector
        y = vector * y_vector
        return engine.entity.base.BasicEntity.Point(x * 250 / Set.screen_range, y * 250 / Set.screen_range, 0)

    # 获得新的画布矢量
    def get_new_xy_vector(self):
        player = self.world.player
        canvas_zero = player.location + player.face_to
        x_vector = engine.entity.base.BasicEntity.Point(
            player.face_to.y,
            - player.face_to.x,
            0
        ).to_modulo_one()
        y_vector = engine.entity.base.BasicEntity.Point(
            - player.face_to.z * player.face_to.x,
            - player.face_to.z * player.face_to.y,
            player.face_to.y ** 2 + player.face_to.x ** 2
        ).to_modulo_one()
        # y > 0 时 x 轴正方向为 x 增大方向
        # if ((math.cos(player.face_to.angle_x) > 0 and x_vector.x < 0)
        #     or (math.cos(player.face_to.angle_x) < 0 and x_vector.x > 0)):
        #     x_vector.reverse()
        # if y_vector.z < 0:
        #     y_vector.reverse()
        return x_vector, y_vector, canvas_zero

    # 判断点是否可见
    def is_visible(self, point):
        player = self.world.player
        A = player.face_to.x
        B = player.face_to.y
        C = player.face_to.z
        return A * point.x + B * point.y + C * point.z \
               > player.location.x * A + player.location.y * B + player.location.z * C

    # 每个tick时执行该函数绘制画面
    def tick_draw(self, dt):
        self.plane = self.canvas_plane()
        x_vector, y_vector, canvas_zero = self.get_new_xy_vector()

        canvas_point_list = []
        canvas_point_visible = []

        # 移动人物
        InputControl.player_move(dt)
        print(World.player)

        # 取出当前世界中的点进行计算，转换到画布坐标系上
        for point in self.world.point_list:
            space_point = self.canvas_plane_cross_point(point)
            canvas_point = self.space_to_canvas(space_point, x_vector, y_vector, canvas_zero)
            screen_reset = engine.entity.base.BasicEntity.Point(
                Set.screen_width / 2,
                Set.screen_height / 2,
                0
            )
            canvas_point_list.append(canvas_point + screen_reset)
            canvas_point_visible.append(self.is_visible(point))
        # 清除画布
        self.window.clear()
        # 重新绘制画布
        print(canvas_point_list)
        for line in self.world.line_list:
            if canvas_point_visible[line[0]] and canvas_point_visible[line[1]]:
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
