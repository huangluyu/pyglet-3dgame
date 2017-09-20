import pyglet, math, time
import CoordinateTurn

window = pyglet.window.Window(800, 600)
label = pyglet.text.Label('去你妈的祖国的花朵',
                          font_name = 'Times New Roman',
                          font_size = 36,
                          x = window.width//2, y = window.height//2,
                          anchor_x = 'center', anchor_y = 'center')
player_ship = pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
                         ('v2i', (10, 15, 30, 35)),
                         ('c3B', (0, 0, 255, 0, 255, 0))
                         )


class Player:
    location = CoordinateTurn.Point
    faceTo = CoordinateTurn.Vector

    def __init__(self, location, faceTo):
        self.location = location
        self.faceTo = faceTo


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


def change_angle(dt):
    window.clear()
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


pyglet.clock.schedule_interval(change_angle, 1/60.0)
pyglet.app.run()