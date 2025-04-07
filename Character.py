class 캐릭터:
    def __init__(self, name="None", hp=100, mp=10, dmg=1):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg= dmg

    def 평타(self, target):
        if(self.target_hp_check(target, self.dmg)):
            print(f" {target.name}에게 {self.dmg}딜")
            target.hp -= self.dmg
    
    def target_hp_check(self, target, skill_dmg):
        if target.hp < skill_dmg:
            target.hp = 0
            print(f" 전투 중 {target.name} 사망")
            return False
        else: #뎀 들어가도 죽지는 않을경우
            return True        
        
    def show_status(self):
        print(f"이름 : {self.name}\n HP : {self.hp}\n MP : {self.mp}")
    
    


class 전사(캐릭터):
    def __init__(self,name):
        super().__init__(name=name, hp = 300, mp =0, dmg = 30)
    def smite(self, target):
        #강타라 평딜의 2배
        skill_dmg = self.dmg * 2
        
        if(self.target_hp_check(target, skill_dmg)):
            print(f" {target.name}에게 {skill_dmg}딜")
            target.hp -= skill_dmg

class 마법사(캐릭터):
    def __init__(self, name):
        super().__init__(name=name, hp=100, mp=300, dmg=1)
    
    def spark(self, target):
        skill_dmg = 120
        
        if(self.target_hp_check(target, skill_dmg)):
            print(f" {target.name}에게 {skill_dmg}딜")
            target.hp -= skill_dmg            

class 스킬:
    def __init__(self, name="스킬명", mp = 0, dmg = 1):
        self.name = name
        self.mp = mp
        self.dmg = dmg
        
        
        

"""
attack 메서드 구현
0. 캐릭터 인스턴스를 두개 만든다
1. 다른 캐릭터 인스턴스를 메서드 인자로 받는다
2. 그 인스턴스의 hp를 깎는다
3. 나온다

상속 클래스 구현
1. 상속 클래스 어떻게 만드는지 물어본다
2. 아래대로 만든다

전사 - 강타, 연속타, 방어 - mp소모량 없음
마법사 - 은신 , 섬광, 점화, 마나뺏기 - mp소모량 80 50 50 0
궁수 - 히트앤런, 헤드샷, 덪깔기 - mp소모량 30, 0, 10

스킬 클래스 구현
1. switch 문으로 스킬명에 따라 기능을 나눈다
"""
