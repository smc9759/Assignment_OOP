from abc import ABC, abstractmethod

class Role(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def 평타(self):
        pass

class Warrior(Role):
    def __init__(self):
        pass
    def 평타(self, character_instance, target):
        target.base_stat.hp -= character_instance.stat.dmg        