import random
from draw import draw_d6

class Player:
    def __init__(self, name: str, departments: str):
        self.name = name
        self.departments = departments.capitalize()

        self.level = 1

        self.fortitude = 1
        self.prudence = 1
        self.temperance = 1
        self.justice = 1

    def print_character_sheet(self):
        print("Lobotomy Corporation Branch 13 ID Card")
        print("Name: "+self.name)
        print("Department: "+self.departments)
        print("Rank: "+str(self.level))
        print("Employee Proficiency Rankings")
        print("Fortitude: "+str(self.fortitude))
        print("Prudence: "+str(self.prudence))
        print("Temperance: "+str(self.temperance))
        print("Justice: "+str(self.justice))

    def roll(self)->int:
        r = random.randint(1, 6)
        mainroll = draw_d6(r)+draw_d6(r)
        return mainroll