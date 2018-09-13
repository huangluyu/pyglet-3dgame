import pyglet
from pyglet.window import key

from engine.control.InputControl import InputControl
from engine.entity.World import World


class Window(pyglet.window.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

    def on_draw(self):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        World.player.face_up(-dy)
        World.player.face_left(-dx)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.W:
            InputControl.keyMap['w'] = True
        if symbol == key.S:
            InputControl.keyMap['s'] = True
        if symbol == key.A:
            InputControl.keyMap['a'] = True
        if symbol == key.D:
            InputControl.keyMap['d'] = True
        if symbol == key.SPACE:
            InputControl.keyMap['space'] = True
        if symbol == key.C:
            InputControl.keyMap['c'] = True
        if symbol == key.LSHIFT:
            InputControl.keyMap['shift'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.W:
            InputControl.keyMap['w'] = False
        if symbol == key.S:
            InputControl.keyMap['s'] = False
        if symbol == key.A:
            InputControl.keyMap['a'] = False
        if symbol == key.D:
            InputControl.keyMap['d'] = False
        if symbol == key.SPACE:
            InputControl.keyMap['space'] = False
        if symbol == key.C:
            InputControl.keyMap['c'] = False
        if symbol == key.LSHIFT:
            InputControl.keyMap['shift'] = False
