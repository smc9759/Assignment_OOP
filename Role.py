from abc import ABC, abstractmethod
from Stat import 스탯
from json_loader import ROLE_STAT_CONFIG

class Role(ABC):
    def __init__(self, base_stat=ROLE_STAT_CONFIG["초보자"]):
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
        1) 직업 인스턴스가 변경될 일이 없음
        2) 메모리 절약하려고 하나 만들어서 공유함
    Args:
        Role (_type_): _description_
    """
    def __init__(self):
        #super 쓸거면 매개변수 이름까지 같아야됨
        #기존 오류 코드 : stat=ROLE_STAT_CONFIG["전사"])
        super().__init__(base_stat=ROLE_STAT_CONFIG["전사"])
    def 평타(self, character_instance, target):
        user = character_instance
        dmg = user.stat.dmg
        if target.stat.hp_check(dmg):
            print(f"{target.name}에게 {dmg} 평타 피해!")
            target.base_stat.hp -= dmg
    
    def use_skill(self, character_instance, target):
        # 전사의 '강타' : 평타 2배
        user = character_instance
        skill_dmg = user.stat.dmg * 2
        if target.stat.hp_check(skill_dmg):
            print(f"{target.name}에게 {skill_dmg} 물리 피해!")
            target.base_stat.hp -= skill_dmg
    
class Mage(Role):
    def __init__(self):
        super().__init__(base_stat=ROLE_STAT_CONFIG["마법사"])
    def 평타(self, user, target):
        dmg = user.stat.dmg
        if target.stat.hp_check(dmg):
            print(f"{target.name}에게 {dmg} 평타 피해!")
            target.base_stat.hp -= dmg
    def use_skill(self, character_instance, target):
        # spark : 60 + dmg
        user = character_instance
        skill_dmg = 60 + (user.stat.dmg * 2)     
        if(target.stat.hp_check(skill_dmg)):
            print(f"{target.name}에게 {skill_dmg} 마법 피해")
            target.base_stat.hp -= skill_dmg  

WARRIOR = Warrior() 

MAGE = Mage()

    
"""
포함 관계가 아닌 '구성' 관계를 만드는 방법
캐릭터는 인벤토리, 스탯, 스킬을 가지고 있지만,
인벤토리 is a 캐릭터 (X)
캐릭터 Has a 인벤토리 (O)
 
"""