import random
from draw import draw_d20

class Player:
    def __init__(self, name: str, departments: str):
        self.name = name
        self.departments = departments

        self.level = 1

        self.fortitude = 0
        self.prudence = 0
        self.temperance = 0
        self.justice = 0

    def print_character_sheet(self):
        print("Lobotomy Corporation Branch 13 ID Card")
        print("Name: "+self.name)
        print("Department: "+self.departments)
        print("Rank: "+str(self.level))
        print("")

    def roll(self)->int:
        r = random.randint(1, 20)
        draw_d20(r)
        return r

