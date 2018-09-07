import engine.entity.static.BasicEntity
import engine.entity.base.BasicEntity
import engine.entity.base.StaticEntity


class Scene:

    @staticmethod
    def load_cube_3x4():
        # 设置场景方块
        cube_list = [
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 200, 200), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 200, 400), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 200, 600), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 200, 800), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 400, 200), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 400, 400), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 400, 600), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 400, 800), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 600, 200), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 600, 400), 200),
            # engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 600, 600), 200),
            engine.entity.static.BasicEntity.Cube(engine.entity.base.BasicEntity.Point(0, 600, 800), 200)
        ]
        return cube_list
