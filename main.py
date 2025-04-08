from Character import character
from Role import Role, WARRIOR, MAGE

#클래스가 아닌 인스턴스로 넘겨야됨
#오류 코드 :                    , Warrior)
#수정 코드 :                    , Warrior())
#더좋은 코드 (인스턴스 하나를 공유)
warrior = character("망치할아범", WARRIOR)

mage = character("숟가락장인", MAGE)

mage.평타(warrior)
warrior.평타(mage)
mage.use_skill(warrior)
warrior.use_skill(mage)

warrior.show_status()
mage.show_status()