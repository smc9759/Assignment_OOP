from abc import ABC, abstractmethod

class Skill(ABC):
    """_summary_
    Skill 추상 클래스
    모든 스킬은 'use' 메서드를 오버라이드하여 구현해야 함.
    Args:
        ABC (_type_): _description_
    """
    def __init__(self):
        pass
    @abstractmethod
    def use(self, caster, target):
        """_summary_
            - caster.stat.dmg 을 통해 능력치를 참조
        Args:
            caster (_type_): 스킬을 시전하는 캐릭터 인스턴스
            target (_type_): 스킬의 대상 캐릭터 인스턴스
        """
        pass
    
class Spark(Skill):
    def __init__(self):
        super().__init__()
        
    def use(self, caster : 'Character', target : 'Character'):
        skill_dmg = 60 + (caster.stat.dmg * 2)     
        if(target.stat.hp_check(skill_dmg)):
            print(f"{target.name}에게 {skill_dmg} 마법 피해")
            target.base_stat.hp -= skill_dmg  
            
class Smite(Skill):
    def __init__(self):
        super().__init__()
        
    def use(self, caster : 'Character', target : 'Character'):
        skill_dmg = caster.stat.dmg * 2
        if target.stat.hp_check(skill_dmg):
            print(f"{target.name}에게 {skill_dmg} 물리 피해!")
            target.base_stat.hp -= skill_dmg
    
    """
    할일 : 전사 클래스의 스킬을 추가한다
    set_skill메서드로 스킬을 골라서 사용할 수 있다
    평타, Q, W, E, R 순으로
    """