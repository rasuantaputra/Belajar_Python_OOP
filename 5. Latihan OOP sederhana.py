class Hero:
    def __init__(self, name, health, attackPower, armorNumber) -> None:
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
        pass
    
    def serang(self, heroName):
        print(self.name, 'menyerang', heroName.name)
        heroName.diserang(self, self.attackPower)

    def diserang(self, heroName, attakPower_lawan):
        print(self.name, 'diserang', heroName.name)
        attack_diterima = attakPower_lawan/self.armorNumber
        print('serangan terasa :', attack_diterima)
        self.health -= attack_diterima
        print('darah', self.name, 'tersisa', self.health)

sniper = Hero('sniper', 100, 10, 5)
gondar = Hero('gondar', 100, 5, 10)

sniper.serang(gondar)