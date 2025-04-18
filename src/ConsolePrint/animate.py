import time
import os
import functools
from random import choice
from .ansi import __ansify_color, DimensionExceptionError
from .logo import image, version


COLORS = ['default', 'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bold']

def keyboard_interrupt(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):        
        try:
            func(*args,**kwargs)
        except KeyboardInterrupt:
            print('\033[0m')
            raise
    return wrapper
            
           
def terminal_width():
    return os.get_terminal_size().columns


def is_width_ok(terminal_width, *text_length):
    if terminal_width <= sum([*text_length]):
        raise DimensionExceptionError("Terminal width is too small to display the output")


@keyboard_interrupt 
def printing(text: str, *, delay: float=0.05, style: str='letter', stay: bool=True, rev: bool=False, format: str='default'):
    """
    Prints text to console letter by letter or word by word forward or in reverse with the chosen format
    """
    width = terminal_width()
    is_width_ok(width, len(text))
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
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
        print("\033[0m")
    print('\033[0m' + ' ' * width, end='\r')


@keyboard_interrupt 
def flashprint(text: str, *, blinks: int=5, delay: float=0.2, stay: bool=True, format: str='default'):
    """
    Makes the text printed to the terminal blink a specified number of times
    """
    width = terminal_width()
    is_width_ok(width, len(text))
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
    for _ in range(blinks):
        print(text, end='\r'), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay:
        print(text)
    print('\033[0m' + ' ' * width, end='\r')


@keyboard_interrupt 
def flashtext(phrase: str, text: str, *, index='end', blinks: int=5, delay: float=0.2, format: str='default'):
    """
    Hilights the chosen key word by flashing it
    """
    width = terminal_width()
    is_width_ok(width, len(text), len(phrase), 1)
    format = __ansify_color(format)
    print(format, end='\r')
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
    print('\033[0m' + ' ' * width, end='\r')


@keyboard_interrupt 
def animate1(text: str, *, symbol: str="#", format: str='default'):
    """
    Flashing masked text to transition to flasing text
    """
    width = terminal_width()
    is_width_ok(width, len(text))
    if len(symbol) != 1:
        raise ValueError("Symbol input should be a single character")
    format = __ansify_color(format)
    text = text.strip()
    symbol = len(text) * symbol
    flashprint(symbol, blinks=3, stay=False, format=format)
    flashprint(text, blinks=2, stay=True, format=format)
    print('\033[0m' + ' ' * width, end='\r')


@keyboard_interrupt 
def animate2(text: str, *, symbol: str="#", delay: float=0.05, format: str='default'):
    """
    Reveals all characters text by text but first masked then flashes
    """
    width = terminal_width()
    is_width_ok(width, len(text))
    if len(symbol) != 1:
        raise ValueError("Symbol input should be a single character")
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
    symbol = len(text) * symbol
    for _ in symbol + "\r" + text + "\r":
        print(_, end="", flush=True)
        time.sleep(delay)
    flashprint(text, blinks=2, stay=True, format=format)
    print('\033[0m' + ' ' * width, end='\r')


@keyboard_interrupt 
def text_box(text: str, *, symbol: str="#", spread: bool=False, padding: bool=False, wall: bool=True, align: str|int="center", format: str='default'):
    """
    Prints text in a box of your chosen symbols.
    If the align parameter is a number then the box is indented by the number count
    """
    width = terminal_width()
    if spread:
        text = " ".join(list(text)).upper()
    if len(symbol) != 1:
        raise ValueError("Symbol input should be a single character")
    format = __ansify_color(format)    
    text = text.strip()
    end = 5 if padding else 3
    text_row = 3 if padding else 2
    length = len(text) + 8
    left_border = text_row - 1  if padding else text_row
    right_border = text_row + 1 if padding else text_row
    is_width_ok(width, len(text), 8, align if isinstance(align, int) else 0)
    if align == "left": indent = 0
    elif align == "right": indent = width - length
    elif align == "center": indent = width//2 - length//2
    elif isinstance(align, int) and align <= (width - length): indent = align
    else: 
        raise ValueError(f"Error in the align argument: {align=}")  
    
    print(format, end='\r')
    for row in range(1, end + 1):
        for col in range(1, length + 1):
            if col == 1:
                print('\033[0m' + (" " * indent) + format, end="")
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
                print('\033[0m')
                

@keyboard_interrupt               
def star_square(num: int, *, symbol: str="#", align: str|int='center', flush: bool=True, format: str='default'):
    """
    Easter egg. 
    Draws a square with the chosen symbol
    """
    width = terminal_width()
    is_width_ok(width, num)
    if len(symbol) != 1:
        raise Exception("Symbol input should be a single character")
    format = __ansify_color(format)
    print(format, end='\r')
    if num < 5 or num > width or not isinstance(num, int):
        print('\033[0m\r')
        raise DimensionExceptionError(f"Invalid square size. Number must be an integer greater than 4 and less than the terminal width: {width}")
    elif align == 'center':
        indent = '\033[0m' + (' ' * (width//2 - num//2)) + format
    elif align == 'right':
        indent = '\033[0m' + (' ' * (width - num)) + format
    elif align == 'left':
        indent = ''  
    elif isinstance(align, int) and width - align > num:
        indent = '\033[0m' + (" " * align) + format
    else:
        print('\033[0m\r')
        raise DimensionExceptionError("Check align parameter and square size with respect to terminal width")    
          
    for row in range(1, num + 1):
        time.sleep(0.04)
        print(indent, end="")
        for col in range(1, num + 1):
            if flush: time.sleep(0.04)                
            if row == 1 or col == 1 or row == num or col == num:
                print(symbol, end="", flush=flush)
            elif row == col:
                print(symbol, end="", flush=flush)
            elif row + col == num + 1:
                print(symbol, end="", flush=flush)  
            else:
                print(" ", end="", flush=flush)              
            if col == num:
                print('\033[0m')
    

@keyboard_interrupt 
def asteriskify(text: str, *, align: str="center", underscore: bool=True, format: str='default'):
    """
    Align text left, center, right or at chosen index and underline it with '*'
    """
    width = terminal_width()
    is_width_ok(width, len(text))
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
    length = len(text)
    
    if align == 'center':
        indent = '\033[0m' + ' ' * (width//2 - length//2) + format
    elif align == 'right':
        indent = '\033[0m' + ' ' * (width - length) + format
    elif align == 'left':
        indent = ''
    else:
        print('\033[0m\r')
        raise Exception("Align argument error") 
    print(indent + text + '\033[0m')
    if underscore:
        print(indent + '*' * length + '\033[0m' + ' ' * (width + 9 - (length + len(indent))))


@keyboard_interrupt
def print_logo(delay=0.1,):
    try:
        is_width_ok(terminal_width(), 69)
        for line in image.split('\n'):
            print(__ansify_color(choice(COLORS)) + line + __ansify_color('default'))
            time.sleep(delay)
    except DimensionExceptionError:
        print('\033[91mTerminal width is too small to display ascii image\033[0m')
    

def terminal_test():
    print_logo()
    printing("hello this should print letter by letter ", delay=0.05, style="letter", stay=True, rev=False, format='red_bg')
    printing("hello this should print word by word but in reverse", delay=0.3, style="word", stay=True, rev=True, format='green_bg')
    flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True, format='blue_bg')
    flashtext("The text in  should flash", "UPPER CASE", blinks=5, index=12, delay=0.2, format='italics')
    animate1("This text is animated with #", symbol="#", format='red_bg')
    animate2("Prints letter by letter but masked with # first  ", symbol="#", delay=0.05, format="\033[48;5;150m")
    text_box("boxed in", symbol="#", padding=False, wall=True, align='center', spread=True, format='\033[48;5;4m')
    asteriskify('This has been asteriskified', align='right', underscore=True, format='cyan_bg')
    print(f'\033[94mThank you for using ConsolePrint v{version}\033[0m')
        
        
if __name__ == "__main__":  
    star_square(10, symbol="@", align=15, flush="True", format="blue_bg")  
    terminal_test()