class Hero :
    # class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor) -> None:
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
        Hero.jumlah_hero += 1
        pass

    # void function, methods tanpa return, tanpa argume
    def siapa(self):
        print('hallo nama saya', self.name)

    # methods dengan argumen tanpa return
    def health_up(self, up):
        self.health += up

    # methode dengan return
    def get_health(self):
        return self.health

hero1 = Hero('sniper', 50, 400, 100)
hero2 = Hero('Mirana', 100, 100, 350)
hero3 = Hero('Ucup', 200, 170, 180)

hero1.siapa()
hero2.health_up(30)

print(hero2.health)
# menggunakan methods
print(hero2.get_health())