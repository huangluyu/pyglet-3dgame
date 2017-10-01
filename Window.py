import pyglet
from pyglet.window import key


class Window(pyglet.window.Window):
    world = None

    def __init__(self, world, width, height):
        super().__init__(width, height)
        self.world = world

    def on_draw(self):
        radius = 100

    def on_mouse_motion(self, x, y, dx, dy):
        player = self.world.player
        player.face_up(-dy)
        player.face_left(-dx)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            self.world.player.speed['w'] = True
        if symbol == key.S:
            self.world.player.speed['s'] = True
        if symbol == key.A:
            self.world.player.speed['a'] = True
        if symbol == key.D:
            self.world.player.speed['d'] = True
        if symbol == key.SPACE:
            self.world.player.speed['space'] = True
        if symbol == key.C:
            self.world.player.speed['c'] = True
        if symbol == key.LSHIFT:
            self.world.player.speed['shift'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            self.world.player.speed['w'] = False
        if symbol == key.S:
            self.world.player.speed['s'] = False
        if symbol == key.A:
            self.world.player.speed['a'] = False
        if symbol == key.D:
            self.world.player.speed['d'] = False
        if symbol == key.SPACE:
            self.world.player.speed['space'] = False
        if symbol == key.C:
            self.world.player.speed['c'] = False
        if symbol == key.LSHIFT:
            self.world.player.speed['shift'] = False
