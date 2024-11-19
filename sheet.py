import random
from draw import draw_d20

class Player:
    def __init__(self, name: str, departments: str):
        self.name = name
        self.departments = departments

        self.level = 1

        self.fortitude = 1
        self.prudence = 1
        if name == "Brandon":
            self.prudence = 2
        self.temperance = 1
        self.justice = 1

        if name == 'Brandon':
            self.prudence = 2

    def print_character_sheet(self):
        print("Lobotomy Corporation Branch 13 ID Card")
        print("Name: "+self.name)
        print("Department: "+self.departments)
        print("Rank: "+str(self.level))
        print("Employee Proficiency Rankings")
        print("Fortitude: "+self.fortitude)
        print("Prudence: "+self.prudence)
        print("Temperance: "+self.temperance)
        print("Justice: "+self.justice)

    def roll(self)->int:
        r = random.randint(1, 20)
        draw_d20(r)
        return r

