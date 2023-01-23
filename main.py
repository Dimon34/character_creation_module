from random import randint


class Character:
    '''Принимает вводимые игроком Имя и Класс'''
    def __init__(self, char_name):
        self.char_name = char_name


    def attack(self):
        return (f'{self.name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):
    pass


class Mage(Character):
    pass


class Healer(Character):
    pass