import time
import os
import re

version = "1.9.3"  # Change version in pyproject

print('\033[0m', end="\r")
__terminal_width = os.get_terminal_size().columns


class DimensionExceptionError(Exception):
    """Custom error when the terminal width is too small"""
    def __init__(self, error_message):
        # self.error_message = error_message
        super().__init__(error_message)


class FormatArgumentError(Exception):
    """Incorrect ANSI sequence passed"""
    def __init__(self, error_message):
        # self.error_message = error_message
        super().__init__(error_message)


def __ansify_color(color: str):  
    match color:
        case 'default': color = '\033[0m'
        case 'grey': color = '\033[30m'
        case 'red': color = '\033[31m'
        case 'green': color = '\033[32m'
        case 'yellow': color = '\033[33m'
        case 'blue': color = '\033[34m'
        case 'magenta': color = '\033[35m'
        case 'cyan': color = '\033[36m'
        case 'white': color = '\033[37m'
        case 'bold': color = '\033[1m'
        case 'italics': color = '\033[3m'
        case 'underscore': color = '\033[4m'
        case 'strike': color = '\033[9m'
        case 'double_under': color = '\033[21m'
        case 'red_bg': color = '\033[41m'
        case 'green_bg': color = '\033[42m'
        case 'yellow_bg': color = '\033[43m'
        case 'blue_bg': color = '\033[44m'
        case 'magenta_bg': color = '\033[45m'
        case 'cyan_bg': color = '\033[46m'
        case 'white_bg': color = '\033[47m'
        case 'italics': color = '\033[3m'
        case _:
            pattern1 = "\\033\\[(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])m"
            pattern2 = "\\033\\[48;5;(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])m"            
            if not (re.fullmatch(pattern1, color) or re.fullmatch(pattern2, color)):
                raise FormatArgumentError("Invalid ANSI escape sequence for argument format")
    return color


def is_width_ok(*text_length):
    if __terminal_width <= sum([*text_length]):
        raise DimensionExceptionError("Terminal width is too small to display text output")


def printing(text: str, *, delay: float=0.05, style: str='letter', stay: bool=True, rev: bool=False, format: str='default'):
    """Prints text to console letter by letter or word by word"""
    is_width_ok(len(text))
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
    print('\033[0m' + ' ' * __terminal_width, end='\r')


def flashprint(text: str, *, blinks: int=5, delay: float=0.2, stay: bool=True, format: str='default'):
    """Gets printed output to blink"""
    is_width_ok(len(text))
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
    for _ in range(blinks):
        print(text, end='\r'), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay:
        print(text)
    print('\033[0m' + ' ' * __terminal_width, end='\r')


def flashtext(phrase: str, text: str, *, index='end', blinks: int=5, delay: float=0.2, format: str='default'):
    """Hilights key word by flashing it"""
    is_width_ok(len(text), len(phrase), 1)
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
    print('\033[0m' + ' ' * __terminal_width, end='\r')


def animate1(text: str, *, symbol: str="#", format: str='default'):
    """Flashing masked text to transition to flasing text"""
    is_width_ok(len(text))
    if len(symbol) != 1:
        raise ValueError("Symbol input should be a single character")
    format = __ansify_color(format)
    text = text.strip()
    symbol = len(text) * symbol
    flashprint(symbol, blinks=3, stay=False, format=format)
    flashprint(text, blinks=2, stay=True, format=format)
    print('\033[0m' + ' ' * __terminal_width, end='\r')


def animate2(text: str, *, symbol: str="#", delay: float=0.05, format: str='default'):
    """Reveals all characters text by text but first masked then flashes"""
    is_width_ok(len(text))
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
    print('\033[0m' + ' ' * __terminal_width, end='\r')


def text_box(text: str, *, symbol: str="#", spread: bool=False, padding: bool=False, wall: bool=True, align: str|int="center", format: str='default'):
    """Prints text in a box of symbols.
If the align parameter is a number then the box is indented by the number count"""
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
    is_width_ok(len(text), 8, align if isinstance(align, int) else 0)
    if align == "left": indent = 0
    elif align == "right": indent = __terminal_width - length
    elif align == "center": indent = __terminal_width//2 - length//2
    elif isinstance(align, int) and align <= (__terminal_width - length): indent = align
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
                
                
def star_square(num: int, *, symbol: str="#", align: str|int='center', flush: bool=True, format: str='default'):
    is_width_ok(num)
    if len(symbol) != 1:
        raise Exception("Symbol input should be a single character")
    format = __ansify_color(format)
    print(format, end='\r')
    if num < 5 or num > __terminal_width or not isinstance(num, int):
        print('\033[0m\r')
        raise DimensionExceptionError(f"Invalid square size. Number must be an integer greater than 4 and less than the terminal width: {__terminal_width}")
    elif align == 'center':
        indent = '\033[0m' + (' ' * (__terminal_width//2 - num//2)) + format
    elif align == 'right':
        indent = '\033[0m' + (' ' * (__terminal_width - num)) + format
    elif align == 'left':
        indent = ''  
    elif isinstance(align, int) and __terminal_width - align > num:
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
    

def asteriskify(text: str, *, align: str="center", underscore: bool=True, format: str='default'):
    is_width_ok(len(text))
    format = __ansify_color(format)
    print(format, end='\r')
    text = text.strip()
    length = len(text)
    
    if align == 'center':
        indent = '\033[0m' + ' ' * (__terminal_width//2 - length//2) + format
    elif align == 'right':
        indent = '\033[0m' + ' ' * (__terminal_width - length) + format
    elif align == 'left':
        indent = ''
    else:
        print('\033[0m\r')
        raise Exception("Align argument error") 
    print(indent + text + '\033[0m')
    if underscore:
        print(indent + '*' * length + '\033[0m' + ' ' * (__terminal_width + 9 - (length + len(indent))))


def terminal_test():
    printing("hello this should print letter by letter ", delay=0.05, style="letter", stay=True, rev=False, format='red_bg')
    printing("hello this should print word by word but in reverse", delay=0.3, style="word", stay=True, rev=True, format='green_bg')
    flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True, format='blue_bg')
    flashtext("The text in  should flash", "UPPER CASE", blinks=5, index=12, delay=0.2, format='italics')
    animate1("This text is animated with #", symbol="#", format='red_bg')
    animate2("Prints letter by letter but masked with # first  ", symbol="#", delay=0.05, format="\033[48;5;150m")
    text_box("boxed in", symbol="#", padding=False, wall=True, align='center', spread=True, format='\033[48;5;4m')
    asteriskify('This has been asteriskified', align='right', underscore=False, format='cyan_bg')
    print(f'Thank you for using ConsolePrint {version}')
        
        
if __name__ == "__main__":  
    star_square(10, symbol="@", align=15, flush="True", format="blue_bg")  
    terminal_test()