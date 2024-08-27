from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные реализации оружия
class Sword(Weapon):
    def attack(self):
        return "strikes with a sword."

class Bow(Weapon):
    def attack(self):
        return "shoots a bow."

# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} takes {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")
        else:
            print(f"{self.name} tries to attack without weapon!")

# Класс монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"The Monster {self.name} is defeated!")

# Функция для демонстрации боя
def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Пример использования
fighter = Fighter("Fighter")
monster = Monster("Goblin")

# Боец выбирает меч и атакует
sword = Sword()
fighter.change_weapon(sword)
battle(fighter, monster)

# Боец выбирает лук и атакует
bow = Bow()
fighter.change_weapon(bow)
battle(fighter, monster)
