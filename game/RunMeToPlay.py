import pyglet

import engine.entity.base.BasicEntity as BaseEntity
import engine.entity.base.Space
from engine.config import Set
from engine.entity.dynamic.Player import Player
from engine.entity.World import World
from engine.canvas.Canvas import Canvas
from game.Scene import Scene
from engine.control.window import Window

# 初始化 pyglet 窗口
window = Window(Set.screen_width, Set.screen_height)
# 初始化人物位置
player = Player(engine.entity.base.Space.Point(0, 0, 0), engine.entity.base.Space.Vector(0, 0, 0, 100, 0, 90))
# 初始化世界
world = World(player)
# 初始化画布
canvas = Canvas(world, window)

# 初始化实体
cube_list = Scene.load_square()
# 放置实体
world.put(cube_list)

#
# pointA = BaseEntity.Point(-10, 0, 0)
# pointB = BaseEntity.Point(20, 2, 2)
# planeVector = BaseEntity.Vector(0, 1, 0)
# planePoint = BaseEntity.Point(1, 1, 0)
# print(Canvas.plane_cross_line(planePoint, planeVector, pointA, pointB))
# print(Canvas.plane_cross_line(planePoint, planeVector, pointB, pointA))

# 设定时钟周期及绘制类
pyglet.clock.schedule_interval(canvas.tick_draw, Canvas.dt)
# 开始运行 pyglet
pyglet.app.run()
