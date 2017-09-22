import pyglet, math, time
import CoordinateTurn, Player, BasicEntity as BE, World

window = pyglet.window.Window(800, 600)
# window.set_exclusive_mouse(True)
label = pyglet.text.Label('去你妈的祖国的花朵',
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y = window.height//2,
                          anchor_x = 'center', anchor_y = 'center')
player_ship = pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2i', (10, 15, 30, 35)),
                         ('c3B', (0, 0, 255, 0, 255, 0))
                         )


def draw_line(a, b, ta, tb):
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2f', (a, b, ta, tb)),
                         ('c3B', (255, 255, 255, 255, 255, 255))
                         )


def draw_square(radius, angle, k):
    angle *= 2 * math.pi / 360
    pointZeroX = window.width//2
    pointZeroY = window.height//2
    x1 = pointZeroX + radius * math.cos(angle)
    y1 = pointZeroY + radius * math.sin(angle) * k
    x2 = pointZeroX + radius * math.sin(angle)
    y2 = pointZeroY - radius * math.cos(angle) * k
    x3 = pointZeroX - radius * math.cos(angle)
    y3 = pointZeroY - radius * math.sin(angle) * k
    x4 = pointZeroX - radius * math.sin(angle)
    y4 = pointZeroY + radius * math.cos(angle) * k
    draw_line(x1, y1, x2, y2)
    draw_line(x2, y2, x3, y3)
    draw_line(x3, y3, x4, y4)
    draw_line(x4, y4, x1, y1)


angle = 0
player = None
world = None

def change_angle(dt):
    global angle
    radius = 200
    angle = angle + dt * 50
    k = 1
    if(angle >= 360):
        angle = 0
    draw_square(radius, angle, k)


@window.event  
def on_draw():
    radius = 100


@window.event()
def on_mouse_motion(x, y, dx, dy):
    global player
    player.face_up(-dy)
    player.face_left(dx)
    # print(player)


def init():
    global player, world
    player = Player.Player(BE.Point(0, 0, 0), BE.Point(0, 0, 0, 1, 90, 0))
    world = World.World()
    world.put(BE.Cube(BE.Point(0, 0, 100), 200))
    world.put(BE.Cube(BE.Point(200, 200, 100), 200))
    # print


def tick_draw(dt):
    window.clear()
    change_angle(dt)


init()
print(BE.Point(1, 2, 3))
print(BE.Point(0, 0, 0, 3.7, 63.4, 36.6))
pyglet.clock.schedule_interval(tick_draw, 1/60.0)
pyglet.app.run()