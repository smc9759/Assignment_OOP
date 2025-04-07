from abc import ABC, abstractmethod
from json_loader import ROLE_STAT_CONFIG

class Role(ABC):
    @abstractmethod
    def 평타(self):
        pass

class Newbie(Role):
    def 평타(self):
        return super().attack()

class Warrior(Role):
    def __init__(self, name="전사"):
        super().__init__(name, stat=ROLE_STAT_CONFIG["전사"])
    def 평타(self):
        return super().attack()
    
class Mage(Role):
    def __init__(self, name="마법사"):
        super().__init__(name, stat=ROLE_STAT_CONFIG["마법사"])
    def 평타(self):
        return super().attack()
    
"""
포함 관계가 아닌 '구성' 관계를 만드는 방법
캐릭터는 인벤토리, 스탯, 스킬을 가지고 있지만,
인벤토리 is a 캐릭터 (X)
캐릭터 Has a 인벤토리 (O)
 
"""