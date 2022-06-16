class Hero: # tempelate
    # class variable
    jumlah = 0

    def __init__(self, input_name, input_health, input_power, input_armor) -> None:
        # instance variable
        self.name = input_name
        self.health = input_health
        self.power = input_power
        self.armor = input_armor

        Hero.jumlah += 1
        print('membuat hero dengan nama : ', input_name)
        pass

hero1 = Hero('sniper', 50, 400, 100)
hero2 = Hero('Mirana', 100, 100, 350)
hero3 = Hero('Ucup', 200, 170, 180)
