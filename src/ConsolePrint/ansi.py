# Background color: \033[48;5;<color_code>m
# This sequence allows you to set a custom background color for the text. 
# Replace <color_code> with a number between 0 and 255 to specify the desired color. 
# For example, \033[48;5;100m sets the background color to a custom color with code 100.


def ansi_codes():
    print("    Colour Codes")
    for _ in range(0, 108, 2):
        print(f'\033[{_}mANSI- "\\033[{_}m"\033[0m || \033[{_+1}mANSI- "\\033[{_+1}m"\033[0m')
        
    print("\n\n    Background Codes")
    for _ in range(0, 256, 2):
        print(f'\033[48;5;{_}mANSI- "\\033[48;5;{_}m"\033[0m || \033[48;5;{_+1}mANSI- "\\033[48;5;{_+1}m"\033[0m')

if __name__ == "__main__":
    ansi_codes()