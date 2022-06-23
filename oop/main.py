class Hero:
    def __init__(self, name, health, power, defense):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense
        
hero1 = Hero("juang", 100, 15, 10)

print(hero1.__dict__)
