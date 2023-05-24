import time
import os
import shutil

terminal_width, terminal_height = shutil.get_terminal_size()

if __name__ == "__main__":
    os.system('cls')
    print(f'{terminal_width=}, {terminal_height=}')
    print(os.get_terminal_size())


def printing(text: str, delay=0.05, style='letter', stay=True, rev=False):
    """Prints text to console letter by letter or word by word"""
    match rev:
        case False:
            if style.lower() == 'letter':
                for _ in range(len(text)):
                    print(text[:_ + 1], end='\r')
                    time.sleep(delay)
            elif style.lower() == 'word':
                text = text.split(' ')
                for _ in range(len(text)):
                    print(' '.join(text[:_ + 1]), end='\r')
                    time.sleep(delay)
        case True:
            if style.lower() == 'letter':
                for _ in range(len(text)):
                    print(text[-1 - _:], end='\r')
                    time.sleep(delay)
            elif style.lower() == 'word':
                text = text.split(' ')
                for _ in range(len(text)):
                    print(' '.join(text[-1 - _:]), end='\r')
                    time.sleep(delay)
    if stay:
        print()


def flashprint(text: str, blinks=5, delay=0.2, stay=True):
    """Gets printed output to blink"""
    for _ in range(blinks):
        print(text, end='\r'), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay:
        print(text)


def flashtext(phrase: str, text: str, index='end', blinks=5, delay=0.2):
    """Hilights key word by flashing it"""
    textb = ' ' * len(text)
    if index == 'end':
        phrase1 = phrase
        phrase2 = ''
    else:
        phrase1 = phrase[:index]
        phrase2 = phrase[index:]

    for _ in range(blinks):
        print(phrase1 + text + phrase2, end='\r')
        time.sleep(delay)
        print(phrase1 + textb + phrase2, end='\r')
        time.sleep(delay)
    print(phrase1 + text + phrase2)


def animate1(text: str, symbol="#"):
    """Flashing masked text to transition to flasing text"""
    symbol = len(text) * symbol
    flashprint(symbol, blinks=3, stay=False)
    flashprint(text, blinks=2, stay=True)


def animate2(text: str, symbol="#", delay=0.05):
    """Reveals all characters text by text but first masked then flashes"""
    symbol = len(text) * symbol
    for _ in symbol + "\r" + text + "\r":
        print(_, end="", flush=True)
        time.sleep(delay)
    flashprint(text, blinks=2, stay=True)

def text_box(text: str, symbol="#", padding=False, wall=True, align="center"):
    """Prints text in a box of symbols
If the align parameter is a number then the box is indented"""
    end = 5 if padding else 3
    text_row = 3 if padding else 2
    length = len(text) + 8
    left_border = text_row - 1  if padding else text_row
    right_border = text_row + 1 if padding else text_row
    
    if align == "left": indent = 0
    elif align == "right": indent = terminal_width - length
    elif align == "center": indent = terminal_width//2 - length//2
    elif isinstance(align, int): indent = align      
    
    for row in range(1, end + 1):
        for col in range(1, length + 1):
            if col == 1:
                print(" " * indent, end="")
            if row == 1 or row == end or col == 1 or col == length:
                if wall:
                    print(symbol, end="")
                else:
                    if left_border <= row <= right_border:
                        print(" ", end="") 
                    else:
                        print(symbol, end="")
            elif row == text_row:
                if col == 3:
                    print("{:^{}}".format(text, length-2), end="")
            else:
                print(" ", end="")  
            if col == length:
                print()
                
                
def star_square(num: int, symbol="#"):
    if num < 5:
        num = 5
    else:        
        for row in range(1, num + 1):
            time.sleep(0.05)
            for col in range(1, num + 1):
                time.sleep(0.05)
                if row == 1 or col == 1 or row == num or col == num:
                    print(symbol, end="", flush=True)
                elif row == col:
                    print(symbol, end="", flush=True)
                elif row + col == num + 1:
                    print(symbol, end="", flush=True)  
                else:
                    print(" ", end="", flush=True)              
                if col == num:
                    print()
            
# Code test
if __name__ == "__main__":
    printing("hello this should print letter by letter", delay=0.05, style="letter", stay=True, rev=False)
    printing("hello this should print word by word but in reverse", delay=0.05, style="word", stay=True, rev=True)
    flashprint("The entire text should flash", flashes=5, delay=0.2, stay=True)
    flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2)
    animate1("This text is animated with #", symbol="#")
    animate2("Prints letter by letter but masked with # first", symbol="#", delay=0.05)
    text_box("C O D E  B R E A K E R", symbol="#", padding=True, wall=True, align="center")
    star_square(8, symbol="@")