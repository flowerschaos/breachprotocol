class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

        self.level = 1

        self.strength = 0
        self.perception = 0
        self.endurance = 0
        self.charisma = 0
        self.intelligence = 0
        self.agility = 0
        self.luck = 0

    def print_character_sheet(self):
        print("Name: "+self.name)
        print("Role: "+self.role)
        print("Level: "+self.level)

