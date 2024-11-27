import time
import random
from sheet import Player

def print_dramatic_text(text: str, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

departments = ['control',
    'information',
    'training',
    'safety',
    'central command', 
    'welfare', 
    'disciplinary',
    'record',
    'extraction']
agent_names = [
    'Bong-Bong',
    'Paul',
    'Emma',
    'Arcade',
    'Veronica',
    'Mike',
    'Jaylen',
    'John',
    'Pam'
]
selected_name = agent_names[random.randint(0,len(agent_names)-1)]
selected_department = departments[random.randint(0,len(departments)-1)]

def containment_breach():
    rollin = random.randint(1, 5)
    if rollin == 1:
        print('The sounds of your footsteps are accentuated by nearby... squeaking?')
        print('You are approached by...')
        print_dramatic_text('🐇0-00-00 - \"STANDARD TRAINING-DUMMY RABBIT\"🐇')
        target = 4
        stat_needed = "Fortitude"
    if rollin == 2:
        print('You are approached by...')
        print_dramatic_text('🐏T-02-99 - \"VOID DREAM\"🐏')
        target = 6
        stat_needed = "Temperance"
    if rollin == 3:
        print('One of your fellow Agents, '+selected_name+' from the '+selected_department.capitalize()+' department, walks towards you. But as they approach, you can see that something has gone very wrong.')
        print('You are approached by an employee possessed by...')
        print_dramatic_text('👠O-04-08 - \"RED SHOES\"👠')
        target = 7
        stat_needed = "Fortitude"
    if rollin == 4:
        print('Swords from an unknown angle fly towards you as you walk by a specific containment unit.')
        print('You are approached by...')
        print_dramatic_text('💧O-01-73 - \"THE KNIGHT OF DESPAIR\"💧')
        target = 8
        stat_needed = "Prudence"
    if rollin == 5:
        print('You hear an angelic chorus coming from somewhere. The end is nigh.')
        print('You are approached by...')
        print_dramatic_text('🕊T-03-46 - \"WHITENIGHT\"🕊')
        target = 10
        stat_needed = "Justice"
    print_dramatic_text('COMBAT START!')
    print('You need to roll at least '+target+' in order to beat this encounter using the '+stat_needed+' stat to win this encounter. Type \'roll\' to roll.')
    
if __name__ == '__main__':
    print_dramatic_text('\033[1;31m BREACH PROTOCOL\033[0;0m')
    print_dramatic_text('A high-stakes stint in a Lobotomy Corporation branch!')
    print()
    print('Lobotomy Corporation, as a game, belongs to Project Moon.')
    print('The rolling system in this adventure is taken from the community-made Project Moon TTRPG.')
    print()
    print_dramatic_text('An alarm clock beeps, and you instinctively hit it. The time is 06:42. Time for work.')
    print_dramatic_text('Walking into the elevator after a very rushed morning routine, you tap your ID card onto the elevator.')
    print()
    # collecting user input
    print('What\'s your name?')
    name = input('My name is...  ')
    if name == 'Brandon' or name == 'Mazey':
        print('A sense of scholarly pride overtakes you. +1 Prudence.')
    if name == 'Felix':
        print('A feeling of dread overtakes you.')
    print()
    dept = ""
    print_dramatic_text('There are 9 Departments in your facility. They are, in order,')
    print_dramatic_text('Control')
    print_dramatic_text('Information')
    print_dramatic_text('Training')
    print_dramatic_text('Safety')
    print_dramatic_text('Central Command')
    print_dramatic_text('Welfare')
    print_dramatic_text('Disciplinary')
    print_dramatic_text('Record')
    print_dramatic_text('Extraction')
    print()
    print_dramatic_text('To learn about a Department\'s function, type the name below. If you already know what each department does, or once you\'ve finished reading, type \'skip\'.')
    dept_map = {
        'control': 'Control - Monitoring Abnormalities and planning of courses of action.',
        'information': 'Information - Collection and organization of Abnormality data and construction of solutions to Abnormality-caused problems.',
        'training': 'Training - Composition and regulation of company policy, management procedures, and training programs for new hires.',
        'safety': 'Safety - Establishment of strategies for multiple unfavorable scenarios, as well as construction of safety guidelines.',
        'central command': 'Central Command - Department supervision and management revision.',
        'welfare': 'Welfare - Damage control of Abnormality breaches to Agent wellbeing and construction of programs to better employee health.',
        'disciplinary': 'Disciplinary - Handling of situations requiring force, be it panicking employee or breaching Abnormality.',
        'record': 'Record - Recordkeeping of all information involving the facility.',
        'extraction': 'Extraction - Handling of materials vital to facility upkeep, like Abnormality obtainment or E.G.O. distribution.'
    }
    
    deptinfo = input('Enter the department you\'d like to know more about: ')
    while deptinfo != 'skip':
        while deptinfo not in departments:
            deptinfo = input('Enter the department you\'d like to know more about: ')
        print(dept_map[deptinfo])
        deptinfo = input('Enter the department you\'d like to know more about: ')
    if deptinfo == 'skip':
        print('What department do you work in?')
        dept = input('I work in... ')
        while dept.lower() not in departments:
            print('That can\'t be right.')
            dept = input('I work in... ')
    print()

    player = Player(name, dept)
    print_dramatic_text('You look down at your identification card before sliding it back into your pocket.')
    player.print_character_sheet()
    print()
    print_dramatic_text('As you exit the elevator, stepping into the main room of the '+dept.capitalize()+' department. No chatter. It is dead silent.')
    print()
    print_dramatic_text('Your goal is to find out where everybody has gone.')
    print_dramatic_text('Lobotomy Corporation has many dangerous things within it\'s facilities.')
    print_dramatic_text('Keep your wits close to you and your weapon closer. Good luck, Agent.')
    print()
    print_dramatic_text('The halls seem quiet. Far too quiet. You continue to walk.')
    enCounter = 0
    while enCounter < 5:
        requirement = containment_breach()
        requirement[0]
        requirement[1]
        if requirement[1] == 'Fortitude':
            player.roll_fortitude()
        if requirement[1] == 'Prudence':
            player.roll_prudence()
        if requirement[1] == 'Temperance':
            player.roll_temperance()
        if requirement[1] == 'Justice':
            player.roll_justice()
        enCounter+=1
    if enCounter == 5:
        print("stop pretty please")