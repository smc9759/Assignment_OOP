from abc import ABC, abstractmethod
from Stat import 스탯
from json_loader import ROLE_STAT_CONFIG
from Skill import Spark, Smite

class Role(ABC):
    def __init__(self, base_stat=ROLE_STAT_CONFIG["초보자"], skill = None):
        self.base_stat = base_stat        
    @abstractmethod
    def 평타(self):
        pass
    @abstractmethod    
    def use_skill():
        pass
    
class Newbie(Role):
    def 평타(self):
        return super().attack()

class Warrior(Role):
    """_summary_

    Args:
        Role (_type_): _description_
    """
    def __init__(self,Smite):
        #super 쓸거면 매개변수 이름까지 같아야됨
        #기존 오류 코드 : stat=ROLE_STAT_CONFIG["전사"])
        super().__init__(base_stat=ROLE_STAT_CONFIG["전사"])
        self.skill = Smite
    
    def 평타(self, character_instance, target):
        user = character_instance
        dmg = user.stat.dmg
        if target.stat.hp_check(dmg):
            print(f"{target.name}에게 {dmg} 평타 피해!")
            target.base_stat.hp -= dmg
    
    def use_skill(self, character_instance, target):
        # 전사의 '강타' : 평타 2배
        # self.skill로 Skill과 Smite 클래스를 이미 가지고 왔다
        # Smite 메서드를 직접 호출하지 않고 추상 메서드 use를 호출한다
# 오류  self.skill.Smite.use()
        self.skill.use(character_instance, target)

    
class Mage(Role):
    def __init__(self, Spark):
        super().__init__(base_stat=ROLE_STAT_CONFIG["마법사"])
        self.skill = Spark
    
    def 평타(self, user, target):
        dmg = user.stat.dmg
        if target.stat.hp_check(dmg):
            print(f"{target.name}에게 {dmg} 평타 피해!")
            target.base_stat.hp -= dmg
    
    def use_skill(self, character_instance, target):
        # spark : 60 + dmg
        self.skill.use(character_instance, target)

#변경할 일 없는 클래스는 인스턴스를 하나만 만들어서 공유함 (효과 : 메모리 절약)
WARRIOR = Warrior(Smite()) 
MAGE = Mage(Spark())

    
"""
포함 관계가 아닌 '구성' 관계를 만드는 방법
캐릭터는 인벤토리, 스탯, 스킬을 가지고 있지만,
인벤토리 is a 캐릭터 (X)
캐릭터 Has a 인벤토리 (O)
 
"""