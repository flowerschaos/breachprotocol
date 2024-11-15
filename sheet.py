class Player:
    def __init__(self, name: str, archetype: str):
        self.name = name
        self.archetype = archetype

        self.level = 1

        self.strength = 0
        self.perception = 0
        self.endurance = 0
        self.charisma = 0
        self.intelligence = 0
        self.agility = 0
        self.luck = 0

    def print_character_sheet(self):
        print("Vit-O-Matic Vigor Tester Results...")
        print("Name: "+self.name)
        print("Archetype: "+self.archetype)
        print("Level: "+str(self.level))
        print("Good luck, buckaroo!")
        

