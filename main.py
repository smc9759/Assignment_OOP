from Character import character, 전사, 마법사

warrior = 전사("망치할아범")

mage = 마법사("숟가락장인")

mage.spark(warrior)
warrior.smite(mage)

warrior.show_status()
mage.show_status()