# Background color: \033[48;5;<color_code>m
# This sequence allows you to set a custom background color for the text. 
# Replace <color_code> with a number between 0 and 255 to specify the desired color. 
# For example, \033[48;5;100m sets the background color to a custom color with code 100.

import re

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
        
        
def ansi_codes():
    print("    Colour Codes")
    for _ in range(0, 108, 2):
        print(f'\033[{_}mANSI- "\\033[{_}m"\033[0m || \033[{_+1}mANSI- "\\033[{_+1}m"\033[0m')
        
    print("\n\n    Background Codes")
    for _ in range(0, 256, 2):
        print(f'\033[48;5;{_}mANSI- "\\033[48;5;{_}m"\033[0m || \033[48;5;{_+1}mANSI- "\\033[48;5;{_+1}m"\033[0m')

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


if __name__ == "__main__":
    ansi_codes()