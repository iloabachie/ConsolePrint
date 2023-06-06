# ConsolePrint
This module making printing to the terminal more exciting by animating the text output.
It also makes output richer my modifying the color
You can also save routine console output to a file using the console2file module.
Created using python 3.11

# Installation
You may install it form PyPI.org using the pip command.

pip install ConsolePrint

# Usage
Copy the code below and run it from your IDE, preferable Visual Studio Code.  May not produce the desired output on some terminals.

import ConsolePrint.animate as prt    

import ConsolePrint.console2file as file  

import ConsolePrint.loading as load        

# Test Cases
1.  Here uou may change the arguments as desired

file.startConsoleSave()

'Saves all output between the start and end functions to file.'

from calendar import calendar

print(calendar(2023))

file.endConsoleSave()

2. Here you may use ANSI escape sequences for the format argument and change others as desired.
Preset arguments for format:
//colours
'default':          '\033[0m'
'grey':             '\033[30m'
'red':              '\033[31m'
'green':            '\033[32m'
'yellow':           '\033[33m'
'blue':             '\033[34m'
'magenta':          '\033[35m'
'cyan':             '\033[36m'
'white':            '\033[37m'
//Text Formats
'bold':             '\033[1m'
'italics':          '\033[3m'
'underscore':       '\033[4m'
'strike':           '\033[9m'
'double_under':     '\033[21m'
'red_bg':           '\033[41m'
'green_bg':         '\033[42m'
'yellow_bg':        '\033[43m'
'blue_bg':          '\033[44m'
'magenta_bg':       '\033[45m'
'cyan_bg':          '\033[46m'
'white_bg':         '\033[47m'

prt.printing("hello this should print letter by letter", delay=0.05, style="letter", stay=True, rev=False, format='strike')

prt.printing("hello this should print word by word but in reverse", delay=0.3, style="word", stay=True, rev=True, format='red_bg')

prt.flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True, format='green')

prt.flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2, format='yellow')

prt.animate1("This text is animated with #", symbol="#", format='white')

prt.animate2("Prints letter by letter but masked with # first  ", symbol="#", delay=0.05, format="\033[48;5;150m")

prt.text_box("B O X E D  I N", symbol="#", padding=True, wall=True, align='center', format='\033[48;5;4m')

prt.asteriskify('This has been asteriskified', align='center', underscore=True, format='cyan')

3.  Here, the load time is specified in seconds

load.countdown(5)

load.loading1(10)

print()

load.loading2(5)

print()

load.loading3(5)

# License
This project is given free for use and download under the MIT license.

# Project Status
Still undergoing enhancements.

# How to Contribute
Fork the repository and create your branch from main.
Clone the repository and make your changes.
Run tests and make sure they pass: python -m unittest
Commit your changes and push to your branch.
Create a pull request.

# Support
If you encounter any issues or have questions about the project, please contact me at udemezue@gmail.com.
