class 스탯:
    def __init__(self, hp=0, mp=0, dmg=0):
        self.hp = hp
        self.mp = mp
        self.dmg = dmg

    def __add__(self, other):
        return 스탯(
            hp=self.hp + other.hp,
            mp=self.mp + other.mp,
            dmg=self.dmg + other.dmg
        )
        """_summary_
        연산자 오버로딩딩
        """
    def copy(self):
        return 스탯(self.hp, self.mp, self.dmg)
        """_summary_
        원본 수정 방지
        """
    
    def __repr__(self):
        return f"스탯(hp={self.hp}, mp={self.mp}, dmg={self.dmg})"
    
    #딜이 들어왔을 때
    def hp_check(self, input_dmg):
        if (self.hp < input_dmg):
            self.hp = 0
            print(f"현제 체력이 {self.hp}입니다")
            #캐릭터 상태 사망
            return False
        else:
            return True
    
    
   
 
"""
#할일    
#증가 - 힐이나 장비 추가체력이 들어왔을 때 

hp
mp
dmg
---
hp check
hp 증가
hp 감소


"""