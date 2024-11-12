import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('Geiger-Based Metronome')
    print_dramatic_text('A mildly radioactive adventure set in the Fallout universe')

    strengthNum = 6
    per = 6
    end = 6
    cha = 6
    intel = 6
    agi = 5
    lck = 5

    # collecting user input
    name = input('Name: ')
    strength = ('S - '+strengthNum)
    perception = ('P - '+per)
    endurance = ('E - '+end)
    charisma = ('C - '+cha)
    intelligence = ('I - '+intel)
    agility = ('A - '+agi)
    luck = ('L - '+lck)
    