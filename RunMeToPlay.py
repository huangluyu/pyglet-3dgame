import pyglet
import World, BasicEntity as BE, Canvas, Player, Window, Scene

player = Player.Player(BE.Point(0, 0, 100), BE.Point(0, 0, 0, 100, 0, 90))
world = World.World(player)
window = Window.Window(world, player.personal_set.screen_width, player.personal_set.screen_height)
canvas = Canvas.Canvas(world, window)

cube_list = Scene.Scene.load_cube_3x4()
for cube in cube_list:
    world.put(cube)

pyglet.clock.schedule_interval(canvas.tick_draw, 1/120)
pyglet.app.run()