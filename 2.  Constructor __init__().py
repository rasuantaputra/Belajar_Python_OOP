class Hero:

    def __init__(self, input_name, input_health, input_power, input_armor) -> None:
        self.name = input_name
        self.health = input_health
        # self. (self dot) tidak harus sama dengan input fungsi
        self.kekuatan = input_power 
        self.armor = input_armor
        pass

hero1 = Hero('sniper', 50, 400, 100)
hero2 = Hero('Mirana', 100, 100, 350)
hero3 = Hero('Ucup', 200, 170, 180)

print(hero1.name)
# disesuaikan dengan self.kekuatan
print(hero2.kekuatan)
print(hero3.armor)

# untuk mengatahui atribut apa saja yang dimiliki
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)