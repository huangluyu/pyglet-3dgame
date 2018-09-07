import pyglet

import engine.entity.base.BasicEntity as BaseEntity
from engine.config import Set
from engine.entity.dynamic.Player import Player
from engine.entity.World import World
from engine.canvas.Canvas import Canvas
from game import Scene
from engine.control.window import Window

# 初始化 pyglet 窗口
window = Window(Set.screen_width, Set.screen_height)
# 初始化人物位置
player = Player(BaseEntity.Point(0, 0, 100), BaseEntity.Point(0, 0, 0, 100, 0, 90))
# 初始化世界
world = World(player)
# 初始化画布
canvas = Canvas(world, window)

# 初始化实体
cube_list = Scene.Scene.load_cube_3x4()
# 放置实体
world.put(cube_list)

# 设定时钟周期及绘制类
pyglet.clock.schedule_interval(canvas.tick_draw, Canvas.dt)
# 开始运行 pyglet
pyglet.app.run()
