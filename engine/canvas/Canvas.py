import math
import pyglet

from engine.entity.base import BasicEntity

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

    # 初始化 设置world（保存实体）和window（显示画面）
    def __init__(self, world, window):
        self.world = world
        self.window = window
        # self.window.set_exclusive_mouse(True)

    # 画一条线
    @staticmethod
    def draw_line(a, b, ta, tb, is_visiable):
        blue = (255, 200, 200, 255, 200, 200)
        red = (0, 255, 0, 0, 255, 0)
        white = (255, 255, 255, 255, 255, 255)
        pyglet.graphics.draw(
            2,
            pyglet.gl.GL_LINES,
            ('v2f', (a, b, ta, tb)),
            ('c3B', blue if is_visiable else red)
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

    # 改变角度 用于测试自动旋转
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
        return BasicEntity.Plane(player.face_to.x, player.face_to.y, player.face_to.z, d)

    # 计算目标点与玩家的连线与画布面的交叉点（世界坐标系），也是目标点在画布面上的投影点
    def canvas_plane_cross_point(self, target_point):
        player = self.world.player
        return self.plane_cross_line(player.location + player.face_to, player.face_to, player.location, target_point)
        # mol = player.face_to.modulo_fang()
        # a = player.face_to.x * (target_point.x - player.location.x) \
        #     + player.face_to.y * (target_point.y - player.location.y) \
        #     + player.face_to.z * (target_point.z - player.location.z)
        # k = mol / a if a != 0 else 0
        # plane_x = k * (target_point.x - player.location.x) + player.location.x
        # plane_y = k * (target_point.y - player.location.y) + player.location.y
        # plane_z = k * (target_point.z - player.location.z) + player.location.z
        # return BasicEntity.Point(plane_x, plane_y, plane_z)

    # 计算点和面的交点
    @staticmethod
    def plane_cross_line(plane_point, plane_vector, point_a, point_b):
        mol = (plane_point.x - point_b.x) * plane_vector.x + \
              (plane_point.y - point_b.y) * plane_vector.y + \
              (plane_point.z - point_b.z) * plane_vector.z
        de = plane_vector.x * (point_a.x - point_b.x) + \
             plane_vector.y * (point_a.y - point_b.y) + \
             plane_vector.z * (point_a.z - point_b.z)
        k = mol / de if de != 0 else 0
        # k = k if k > 0 else -k
        # print("k", k, "x", point_a.x - point_b.x, "y", point_a.y - point_b.y, "z", point_a.z - point_b.z)
        cross_point_x = k * (point_a.x - point_b.x) + point_b.x
        cross_point_y = k * (point_a.y - point_b.y) + point_b.y
        cross_point_z = k * (point_a.z - point_b.z) + point_b.z
        return BasicEntity.Point(cross_point_x, cross_point_y, cross_point_z)

    # 空间点投影到画布上获取只有x，y两个坐标的画布点
    # 参数：空间点坐标，画布坐标系 x 轴方向矢量，y 轴方向矢量，画布原点坐标
    @staticmethod
    def space_to_canvas(space_point, x_vector, y_vector, canvas_zero):
        vector = space_point - canvas_zero
        x = vector * x_vector
        y = vector * y_vector
        return BasicEntity.Point(x * 250 / Set.screen_range, y * 250 / Set.screen_range, 0)

    # 获得当前朝向下新的画布面（x轴，y轴，及原点）
    def get_new_xy_vector(self):
        player = self.world.player
        canvas_zero = player.location + player.face_to
        x_vector = BasicEntity.Vector(
            player.face_to.y,
            - player.face_to.x,
            0
        ).to_modulo_one()
        y_vector = BasicEntity.Vector(
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

    # 判断点是否可见（即：是否在后脑勺后面）
    def is_visible(self, point):
        player = self.world.player
        A = player.face_to.x
        B = player.face_to.y
        C = player.face_to.z
        return (A * point.x + B * point.y + C * point.z) > \
               (player.location.x * A + player.location.y * B + player.location.z * C)

    # 每个tick时执行该函数绘制画面
    def tick_draw(self, dt):
        # 移动人物
        InputControl.player_move(dt)

        self.plane = self.canvas_plane()
        x_vector, y_vector, canvas_zero = self.get_new_xy_vector()

        # 存储线及点是否可见
        canvas_point_list = []
        canvas_point_visible = []
        point_list = []

        # 屏幕中点
        screen_reset = BasicEntity.Point(
            Set.screen_width / 2,
            Set.screen_height / 2,
            0
        )

        # 取出当前世界中的点进行计算，转换到画布坐标系上
        for point in self.world.point_list:
            # 简化空间点
            space_point = self.canvas_plane_cross_point(point)
            # 获取画布点（以原点为中心）
            canvas_point = self.space_to_canvas(space_point, x_vector, y_vector, canvas_zero)
            # print("point", point, "space_point", space_point, "canvas_point", canvas_point)
            point_list.append(point)
            # 获取画布点移至视平面中心，并存储至列表中
            canvas_point_list.append(canvas_point + screen_reset)
            # 判断点是否存在于
            canvas_point_visible.append(self.is_visible(point))

        # 清除画布
        self.window.clear()
        # 重新绘制画布，将点的连线应用至点上
        for line in self.world.line_list:
            # 遍历连线
            # 如果连线的两端都不可见则直接跳过
            is_visible = True
            if not canvas_point_visible[line[0]] and not canvas_point_visible[line[1]]:
                continue
            player = self.world.player
            point_a = canvas_point_list[line[0]]
            point_b = canvas_point_list[line[1]]
            print(point_a, point_b)
            if self.is_out_screen(point_a) and self.is_out_screen(point_b):
                continue
            elif self.is_out_screen(point_a) and not canvas_point_visible[line[1]]:
                continue
            elif self.is_out_screen(point_b) and not canvas_point_visible[line[0]]:
                continue
            # 单侧不可见的情况下，将其中转换为投影
            if not canvas_point_visible[line[0]] :
                is_visible = False
                cross_point = self.plane_cross_line(player.location + player.face_to, player.face_to,
                                                point_list[line[0]], point_list[line[1]])

                canvas_cross_point = self.space_to_canvas(cross_point, x_vector, y_vector, canvas_zero)

                point_a = self.get_final_cross_point(point_b, canvas_cross_point + screen_reset)
                print("cross_point", cross_point, "canvas_cross_point", canvas_cross_point, "point_a", point_a)
            elif not canvas_point_visible[line[1]]:
                is_visible = False
                cross_point = self.plane_cross_line(player.location + player.face_to, player.face_to,
                                                point_list[line[0]], point_list[line[1]])
                canvas_cross_point = self.space_to_canvas(cross_point, x_vector, y_vector, canvas_zero)
                point_b = self.get_final_cross_point(point_a, canvas_cross_point + screen_reset)
                print("cross_point", cross_point, "canvas_cross_point", canvas_cross_point, "point_b", point_b)
            # print("point_a", point_a, "point_b", point_b)
            # 绘制连线
            Canvas.draw_line(
                point_a.x, point_a.y,
                point_b.x, point_b.y, is_visible
            )
        # point_a = BasicEntity.Point(700, 550, 0)
        # point_b = BasicEntity.Point(600, 500, 0)
        # cross_point = self.get_final_cross_point(point_b, point_a)
        # print("cross_point", cross_point)
        # Canvas.draw_line(
        #     point_b.x, point_b.y,
        #     cross_point.x, cross_point.y, True
        # )

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

    # 获得画布平面上两点的延长线与画布框的交点
    def get_final_cross_point(self, point_start, point_cross):
        # print("point_start", point_start, "point_cross", point_cross)
        if (point_cross.x > Set.screen_width or point_cross.x < 0) and (point_cross.y > Set.screen_height or point_cross.y < 0):
            return point_cross
        k = self.get_line_k(point_cross, point_start)
        k1 = self.get_line_k(BasicEntity.Point(Set.screen_width, Set.screen_height, 0), point_start)
        k2 = self.get_line_k(BasicEntity.Point(0, Set.screen_height, 0), point_start)
        k3 = self.get_line_k(BasicEntity.Point(0, 0, 0), point_start)
        k4 = self.get_line_k(BasicEntity.Point(Set.screen_width, 0, 0), point_start)
        if k == 0:
            k = 0.001
        # 与画布平面上四条边的四个交点
        point1 = BasicEntity.Point((Set.screen_height - point_start.y) / k + point_start.x, Set.screen_height, 0)
        point2 = BasicEntity.Point(0, - point_start.x * k + point_start.y, 0)
        point3 = BasicEntity.Point(- point_start.y / k + point_start.x, 0, 0)
        point4 = BasicEntity.Point(Set.screen_width, (Set.screen_width - point_start.x) * k + point_start.y, 0)
        # print("point1", point1, k1)
        # print("point2", point2, k2)
        # print("point3", point3, k3)
        # print("point4", point4, k4)
        # print("k", k)
        if point_cross.x >= point_start.x and point_cross.y >= point_start.y:
            if k >= k1:
                return point1
            else:
                return point4
        if point_cross.x < point_start.x and point_cross.y >= point_start.y:
            if k >= k2:
                return point2
            else:
                return point1
        if point_cross.x < point_start.x and point_cross.y < point_start.y:
            if k >= k3:
                return point3
            else:
                return point2
        if point_cross.x >= point_start.x and point_cross.y < point_start.y:
            if k >= k4:
                return point4
            else:
                return point3

    @staticmethod
    def get_line_k(pointA, pointB):
        if pointA.x - pointB.x == 0:
            return (pointA.y - pointB.y) * 1000
        return (pointA.y - pointB.y) / (pointA.x - pointB.x)

    @staticmethod
    def is_out_screen(point):
        return point.x < 0 or point.x > Set.screen_width or point.y < 0 or point.y >= Set.screen_height