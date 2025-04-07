from abc import ABC, abstractmethod

class Role(ABC):
    @abstractmethod
    def 평타(self):
        pass
    
class Warrior(Role):
    def 평타(self):
        return super().attack()
    
"""
포함 관계가 아닌 '구성' 관계를 만드는 방법
캐릭터는 인벤토리, 스탯, 스킬을 가지고 있지만,
인벤토리 is a 캐릭터 (X)
캐릭터 Has a 인벤토리 (O)
 
"""