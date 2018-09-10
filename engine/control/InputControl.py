from engine.canvas import Canvas
from engine.entity.World import World
from engine.entity.base import BasicEntity
from engine.entity.dynamic.Player import Player


class InputControl:
    # 快捷键
    keyMap = dict(w=False, s=False, a=False, d=False, shift=False, space=False, c=False)

    @staticmethod
    def player_move(dt):
        move_to = BasicEntity.Vector(0, 0, 0)
        if InputControl.keyMap["w"]:
            move_to += World.player.face_to * -1
        elif InputControl.keyMap["s"]:
            move_to += World.player.face_to
        if InputControl.keyMap["d"]:
            move_to += BasicEntity.Vector(-World.player.face_to.y, World.player.face_to.x, 0).to_modulo_one() * 100
        elif InputControl.keyMap["a"]:
            move_to += BasicEntity.Vector(World.player.face_to.y, -World.player.face_to.x, 0).to_modulo_one() * 100
        if InputControl.keyMap['space']:
            move_to += BasicEntity.Vector(0, 0, -1).to_modulo_one() * 100
        elif InputControl.keyMap['c']:
            move_to += BasicEntity.Vector(0, 0, 1).to_modulo_one() * 100
        if InputControl.keyMap['shift']:
            move_to *= 3
        World.player.move(move_to * dt)
