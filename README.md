# ConsolePrint Module
This module makes printing to the terminal more exciting by animating the text output.
It also makes the output richer my providing access to color codes for terminal or console applicatons.
You can also save routine console output to a file using the console2file module.
Requires python 3.10 or later versions.

# Installation
You may install it form PyPI.org using the pip command typed in your terminal.<br>
`pip install ConsolePrint`

# Terminal Compatibility
To check for terminal compatibility, run the code below.

```python
import ConsolePrint

ConsolePrint.terminal_test()

```

# Test Cases
1.  This package includes methods for saving the outputs to the terminal in a file.  It can be used as a context manager using the following code.

```python
import ConsolePrint.console2file as file
from calendar import calendar

with file.SaveToFile(name='my_output', prompt=True):        
        print("log 1: Printing Calendar...")
        print(calendar(2025))
        print("log 2: Printing finished...") 
```

Alternatively, run your code between the startConsoleSave and endConsoleSave function calls to save the output to file.  The prompt argument determines if a prompt to open the file is displayed (Windows only).

```python
import ConsolePrint.console2file as file
from calendar import calendar

file.startConsoleSave(name="my_output")

print("log 1: Printing Calendar...")
print(calendar(2025))
print("log 2: Printing finished...") 

file.endConsoleSave(prompt=True)
```

To save the output of a single function, use the func2file decorator.

```python
import ConsolePrint.console2file as file
from calendar import calendar

@file.func2file(filename='function_output', prompt=False)
def calendar_print():
    print("log 1: Printing Calendar...")
    print(calendar(2025))
    print("log 2: Printing finished...")
    return "This output value is also saved to the file."

calendar_print()
```
2.  This module permits differnt colourful print animations to be output to the terminal.  The format argument takes an ANSI escape sequences as a string.  You may also modify other arguments as desired.<br>
To view a full list of all the ANSI escape sequences in the 256-color mode and confirm if your terminal can display the output, import the package and run the code below:

```python
import ConsolePrint
# To view available ANSI codes
ConsolePrint.ansi_codes()

```
The following preset string values may be used instead of the ANSI escape sequences

| Format  | ANSI Code | Format       | ANSI Code |
|---------|-----------|------------- |-----------|
| grey    | \033[30m  | italics      | \033[3m   |
| red     | \033[31m  | underscore   | \033[4m   |
| green   | \033[32m  | strike       | \033[9m   |
| yellow  | \033[33m  | double_under | \033[21m  |
| blue    | \033[34m  | red_bg       | \033[41m  |
| magenta | \033[35m  | green_bg     | \033[42m  |
| cyan    | \033[36m  | yellow_bg    | \033[43m  |
| white   | \033[37m  | blue_bg      | \033[44m  |
| bold    | \033[1m   | magenta_bg   | \033[45m  |
| italics | \033[3m   | cyan_bg      | \033[46m  |
| default | \033[0m   | white_bg     | \033[47m  |

Code usage:

```python 
import ConsolePrint.animate as prt 

prt.printing("hello this should print letter by letter", delay=0.05, style="letter", stay=True, rev=False, format='strike')
prt.printing("hello this should print word by word but in reverse", delay=0.3, style="word", stay=True, rev=True, format='red_bg')
prt.flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True, format='green')
prt.flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2, format='yellow')
prt.animate1("This text is animated with #", symbol="#", format='magenta')
prt.animate2("Prints letter by letter but masked with # first  ", symbol="#", delay=0.05, format="\033[48;5;150m")
prt.text_box("boxed in", symbol="#", padding=True, wall=True, align='right', format='\033[48;5;4m')
prt.asteriskify('This has been asteriskified', align='center', underscore=True, format='cyan')

```

3.  This adds loading animations to terminal output.  The load time argument is specified as an integer in seconds.
```python
import ConsolePrint.loading as load  

load.countdown(5)
load.loading1(10)
print()
load.loading2(5, text='Scanning...')
print()
load.loading3(5)

```
## License
This project is given free for use and download under the MIT license.

## Project Status
Still undergoing enhancements.

## How to Contribute
Fork the repository and create your branch from main.
Clone the repository and make your changes.
Run tests and make sure they pass: python -m unittest
Commit your changes and push to your branch.
Create a pull request.

## Support
If you encounter any issues or have questions about the project, please contact me at udemezue@gmail.com.
