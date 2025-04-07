from abc import ABC, abstractmethod

class Role(ABC):
    @abstractmethod
    def 평타(self):
        pass
    
class Warrior(Role):
    def 평타(self):
        return super().attack()