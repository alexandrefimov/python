class Hero():
    """" Class to create Hero for our game """
    def __init__(self, name, level, race):
        """" Initiate hero """
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """" Print all parameters of hero """
        descripton = ("Name: " + self.name + " Level: " + str(self.level) + " Race: " + self.race + " Health: " + str(self.health)).title()
        print(descripton)

    def level_up(self):
        """Upgrade Level"""
        self.level += 1

    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + " start moving..")

    def set_health(self, new_health):
        self.health = new_health

class SuperHero(Hero):
    """" Class to create superhero """
    def __init__(self, name, level, race, magiclevel):
        """" Initiate superhero """
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def make_magic(self):
        """ Use magic """
        self.magic -= 10

    def show_hero(self):
        """" Print all parameters of hero """
        descripton = ("Name: " + self.name + " Level: " + str(self.level) + " Race: " + self.race + " Health: " + str(self.health) + " Magic: " + str(self.magic)).title()
        print(descripton)