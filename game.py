import time
from sheet import Player

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# def generate_enemy()->int:
    
if __name__ == '__main__':
    print_dramatic_text('\033[1;31m BREACH PROTOCOL\033[0;0m')
    print('A high-stakes stint in a Lobotomy Corporation branch!')
    print()
    print('Lobotomy Corporation, as a game, belongs to Project Moon.')
    print('The rolling system in this adventure is taken from the community-made Project Moon TTRPG.')
    print('Type \'begin workday\' to start.')
    start = input()
    if start == 'begin workday':
        print_dramatic_text('An alarm clock beeps, and you instinctively hit it. The time is 06:42. Time for work.')
        print_dramatic_text('You look down at your ID card as you stand in the elevator after rushing to get ready.')
        print()
        # collecting user input
        print('What\'s your name?')
        name = input('My name is...  ')
        if name == "Brandon":
            print("As you look at your card, a sense of scholarly pride fills you. +1 to Prudence.")
        print()
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
        print('To learn about a Department\'s function, type the name below. If you already know what each department does, type \'skip\'. Once you\'re done reading, type \'skip\'.')
        dept_map = {
            'control': 'Monitoring Abnormalities and planning of courses of action.',
            'information': 'Collection and organization of Abnormality data and construction of solutions to Abnormality-caused problems.',
            'training': 'Composition and regulation of company policy, management procedures, and training programs for new hires.',
            'safety': 'Establishment of strategies for multiple unfavorable scenarios, as well as construction of safety guidelines.',
            'central command': 'Department supervision and management revision.',
            'welfare': 'Damage control of Abnormality breaches to Agent wellbeing and construction of programs to better employee health.',
            'disciplinary': 'Handling of situations requiring force, be it panicking employee or breaching Abnormality.',
            'record': 'Recordkeeping of all information involving the facility.',
            'extraction': 'Handling of materials vital to facility upkeep, like Abnormality obtainment or E.G.O. distribution.'
        }
        departments = ['control',
                    'information',
                    'training',
                    'safety',
                    'central command', 
                    'welfare', 
                    'disciplinary',
                    'record',
                    'extraction']
        deptinfo = input()
        while deptinfo not in departments or deptinfo != 'skip':
            deptinfo = input('Enter the department you\'d like to know more about: ')
            if deptinfo = 'skip':
            message = dept_map[deptinfo]
            print('What department do you work in?')
            dept = input('I work in... ')
            while dept.lower() not in departments:
                print('That can\'t be right.')
                dept = input('I work in... ')
        print()

        player = Player(name, dept)

        player.print_character_sheet()

        roll = player.roll()
    else:
        print('Come on, we both know how this works.')
        start = input()