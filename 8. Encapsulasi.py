# Tujuan dari encapsulasi adalah untuk menjaga agar nilai variabel tidak mudah di ubah dari luar

from queue import PriorityQueue


class Hero:

    def __init__(self, name, health, attackPower) -> None:
        self.__name = name
        self.__health = health
        self.__attPower = attackPower
        pass

    # getter -> agar bisa mendapatkan nilai private variabel
    def getName(self):
        return self.__name
        pass
    
    def getHealth(self):
        return self.__health
        pass

    # setter -> agar bisa merubah nilai private variable
    def diserang(self, powerSerangan):
        self.__health -= powerSerangan
        pass

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru
        pass


# awal dari game
bloodseeker = Hero('Bloodseeker', 50, 7)

# game berjalan
print(bloodseeker.getName())
print(bloodseeker.getHealth())
bloodseeker.diserang(6)
print(bloodseeker.getHealth())