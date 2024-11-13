import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('Geiger-Based Metronome')
    print_dramatic_text('A mildly radioactive adventure set in the Fallout universe')

    # collecting user input
    name = input('Name: ')
    