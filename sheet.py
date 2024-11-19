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

        if name == 'Brandon' or name == 'Mazey':
            self.prudence = 2
        
        if name == 'Felix':
            self.level = 2
            self.fortitude = 3
            self.prudence = 3
            self.temperance = 3
            self.justice = 3

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
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        draw_d6(a)
        draw_d6(b)
        return a+b

    def roll_fortitude(self)->int:
        r = self.roll()
        return r+self.fortitude
    def roll_prudence(self)->int:
        r = self.roll()
        return r+self.prudence
    def roll_temperance(self)->int:
        r = self.roll()
        return r+self.temperance
    def roll_justice(self)->int:
        r = self.roll()
        return r+self.justice