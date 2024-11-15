import time
from sheet import Player

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('Wild Wasteland')
    print_dramatic_text('A mildly radioactive adventure set in the Fallout universe')
    print()
    print_dramatic_text('Our story begins in the Mojave wasteland. The sun rises, hitting your eyes.')
    print()
    # collecting user input
    print('What\'s your name?')
    print()
    name = input('My name is...  ')
    print()
    print('Where do you come from?')
    print()
    print_dramatic_text('Dweller: I hail from Vault 13, a homely place.')
    print_dramatic_text('Raider: I take from others for my own benefit.')
    print_dramatic_text('Wastelander: I\'m just trying to make it through the blisteringly hot days post-War.')
    print_dramatic_text('Knight: I\'m a member of the Brotherhood of Steel, who collect and protect technology.')
    print_dramatic_text('Ranger: I\'m a member of the New California Republic, and are here in the Mojave as a lookout.')
    print_dramatic_text('Legionnaire: As a loyal part of the fearsome Caesar\'s Legion, I have forgone my past as a tribemember and crowned myself with the golden laurels of the Legion.')
    print_dramatic_text('Courier: I am a package courier for the Mojave Express, located in Primm.')
    print_dramatic_text('Follower: I\'m a Follower of the Apocalypse- Despite the name, I\'m dedicated to helping out those around me in the wasteland.')
    arch = input('I am a... ')
    archetypes = ['dweller',
                  'raider',
                  'wastelander',
                  'knight',
                  'ranger', 
                  'legionnaire', 
                  'courier',
                  'follower']
    while arch.lower() not in archetypes:
        print('Say that again?')
        arch = input('I am a... ')
print()
print_dramatic_text('You step up to the \"Vit-O-Matic Vigor Tester\", and a light flickers to life.')
print()
print('You\'re S.P.E.C.I.A.L.! Let\'s see how you do...')
print('You have 40 points to allocate into 8 categories.')
print()
print_dramatic_text('Strength: Raw, physical strength.')
print_dramatic_text('Perception: How well you use your senses.')
print_dramatic_text('Endurance: Health and overall fitness.')
print_dramatic_text('Charisma: Charm and social skills.')
print_dramatic_text('Intelligence: Basic intellect, curiosity in the world and adeptness at critical thinking.')
print_dramatic_text('Agility: Quickness and agility.')
print_dramatic_text('Luck: How often good things happen to you.')

    player = Player(name, arch)

    player.print_character_sheet()

print('The sun beats down on you, as you walk through the wasteland. You\'re trying to get to New Vegas, the legendary city untouched by the nuclear fire that had scorched the rest of the world.')
if arch = knight:
    print('The only sounds you hear are the thumping and hydraulics of the power armor you wear. It\'s far too hot to be shambling around in a hunk of metal, but at least there\'s air conditioning in this exosuit.')
if arch = legionnaire, ranger:
    print('You walk with the rest of your squadron.')
else:
    print('It\'s dead quiet, as per usual.')
print('You are approached by a radscorpion.')
print('Combat start!')
