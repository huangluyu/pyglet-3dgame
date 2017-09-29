import pyglet
from pyglet.window import key
import World, BasicEntity as BE, Canvas, Player, Window

world = World.World(Player.Player(BE.Point(0, 0, 100), BE.Point(0, 0, 0, 100, 0, 90)))
canvas = Canvas.Canvas(world)
window = canvas.window


@window.event()
def on_draw():
    radius = 100


@window.event()
def on_mouse_motion(x, y, dx, dy):
    global world
    player = world.player
    player.face_up(-dy)
    player.face_left(-dx)


@window.event()
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        world.player.speed['w'] = True
        world.player.speed['s'] = False
    elif symbol == key.S:
        world.player.speed['w'] = False
        world.player.speed['s'] = True
    if symbol == key.A:
        world.player.speed['d'] = False
        world.player.speed['a'] = True
    elif symbol == key.D:
        world.player.speed['a'] = False
        world.player.speed['d'] = True
    if symbol == key.SPACE:
        world.player.speed['space'] = True
        world.player.speed['c'] = False
    elif symbol == key.C:
        world.player.speed['space'] = False
        world.player.speed['c'] = True
    if symbol == key.LSHIFT:
        world.player.speed['shift'] = True


@window.event()
def on_key_release(symbol, modifiers):
    if symbol == key.W:
        world.player.speed['w'] = False
    if symbol == key.S:
        world.player.speed['s'] = False
    if symbol == key.A:
        world.player.speed['a'] = False
    if symbol == key.D:
        world.player.speed['d'] = False
    if symbol == key.SPACE:
        world.player.speed['space'] = False
    if symbol == key.C:
        world.player.speed['c'] = False
    if symbol == key.LSHIFT:
        world.player.speed['shift'] = False

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
pyglet.clock.schedule_interval(canvas.tick_draw, 1/120)
pyglet.app.run()