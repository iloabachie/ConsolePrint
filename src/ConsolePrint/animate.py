import time
import os

if __name__ == "__main__":
    os.system('cls')


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

def text_box(text: str, symbol="#", padding=False, wall=True, indent=4):
    """Prints text in a box of symbols"""
    end = 5 if padding else 3
    text_row = 3 if padding else 2
    length = len(text) + 8
    left_border = text_row - 1  if padding else text_row
    right_border = text_row + 1 if padding else text_row
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
                
                
def star_square(num: int, symbol="@"):
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
    printing("This text prints word by word. Cool isn't it?", style='word', delay=0.3)
    printing("This text prints letter by letter and does not move to the new line", 0.06, 'letter', False, False)
    print()
    printing("This text prints letter by letter but in reverse", rev=True)
    flashprint("This entire Text is flashing")
    flashtext('The word at the end of this text is ', 'flashing', delay=0.2, blinks=5)
    animate1("This text is animated with # symbol")
    animate2("This text is animated with # symbol")              
    star_square(8, symbol="&")    
    text_box("C O D E  B R E A K E R", symbol="$", padding=True, wall=True)