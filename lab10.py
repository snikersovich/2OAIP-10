class Resources:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def set_name(self, name):
        self.__name = name

    def set_quantity(self, quantity):
        self.__quantity = quantity


class Tools:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Weapon:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Sword(Weapon):
    def __init__(self):
        super().__init__('Меч')


class Crafting:
    def craft_sword(self, Resource1, Resource2):
        if Resource1.get_name() == 'Железный слиток' and Resource1.get_quantity() >= 2 and Resource2.get_name() == 'Палка' and Resource2.get_quantity() >= 1:
            print('Меч скрафчен')
            return Sword()
        else:
            print('Недостаточно ресурсов для крафта меча')

    def craft_axe(self, Resource1, Resource2):
        if Resource1.get_name() == 'Железный слиток' and Resource1.get_quantity() >= 3 and Resource2.get_name() == 'Палка' and Resource2.get_quantity() >= 2:
            print('Топор скрафчен')
            return Tools
        else:
            print('Недостаточно ресурсов для крафта топора')


Resource1 = Resources('Железный слиток', 2)
Resource2 = Resources('Палка', 2)
Crafting = Crafting()
My_Sword = Crafting.craft_sword(Resource1, Resource2)
My_Axe = Crafting.craft_axe(Resource1, Resource2)