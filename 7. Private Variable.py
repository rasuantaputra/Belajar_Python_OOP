from email.base64mime import header_length
from unicodedata import name


class Hero:

    # membuat private class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # membuat private instance dengan menambah 2 underscore (__)
        self.__iniPrivateinstance = 'private'

        # membuat protect instance dengan menambah 1 underscore (_) 
        self._iniProtectinstance = 'protect'

lina = Hero('slayer', 2000)

print(lina.__dict__)


