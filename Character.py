from Stat import 스탯
from Role import Role, Warrior
#캐릭터 구성하기 1) 스탯
class Player:
    def __init__(self, character):
        self.character = character

class character(Player):
    #어려운 개념 - 포함 관계가 아닌 구성 관계
    def __init__(self, name, role):
        self.name = name
        self.role = role #전사...
        self.base_stat = role.base_stat.copy()
        self.equip_stat = 스탯() #현재 0 (미구현)
    
    @property    
    def stat(self):
        #스탯 클래스끼리 더하기 가능 (연산자 오버로딩)
        return self.base_stat + self.equip_stat

        """_summary_
        
            if stat is not None:
                self.stat = stat
            else:
                self.stat = 스탯()
            
            (C) null = (Python) None 
            비슷한 의미로 쓰인다

            조건문에서 등호보다 is 를 권장한다
            (PEP8) if x == None:  (X)
                if x is None  (O)

            ✅ == vs is 차이
            연산자	의미	예시
            ==	값(value)이 같은지 비교	a == b
            is	객체(object) 자체가 같은지 비교 (같은 메모리 주소인지)
        Returns:
            _type_: _description_
        """

    def 평타(self, target):
        self.role.평타(self, target)

    def use_skill(self, target):
        self.role.use_skill(self, target)  
        
    def show_status(self):
        print(f"이름 : {self.name}\n HP : {self.stat.hp}\n MP : {self.stat.mp}")          
      

"""
#할일 - 평타 맞으면 hp까는 함수에서 base_stat 을 까지않고, 최대 체력에서 까는 방식으로 전환 
# (장비의 유효성에 관한 수정사항)


attack 메서드 구현
0. character 인스턴스를 두개 만든다
1. 다른 character 인스턴스를 메서드 인자로 받는다
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

