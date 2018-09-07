from .BasicEntity import BasicEntity
from abc import abstractmethod


class DynamicEntity(BasicEntity):

    speed = 10

    @abstractmethod
    def move(self, dt):
        pass
