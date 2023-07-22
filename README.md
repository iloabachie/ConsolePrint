# ConsolePrint Module
This module makes printing to the terminal more exciting by animating the text output.
It also makes the output richer my providing access to color modification.
You can also save routine console output to a file using the console2file module.
Requires python 3.10 or later versions.

# Installation
You may install it form PyPI.org using the pip command typed in your terminal.<br>
`pip install ConsolePrint`

# Test Cases
1.  This permits output of programs to be saved in a file.  Run your code between the start and end console save functions to save the output to file.
```python
import ConsolePrint.console2file as file  

file.startConsoleSave(name="my_output.txt", prompt=False)
# Saves all output between the start and end functions to filename argument
from calendar import calendar
print(calendar(2023))
file.endConsoleSave()
```
2.  This module permits differnt colourful print animations to be output to file.  The format argument takes an ANSI escape sequences as a string.  You may also modify other arguments as desired.<br>
To view a full list of all the ANSI escape sequences and confirm if your terminal can display the output, import the package and run the command below:
```python
import ConsolePrint
ConsolePrint.ansi_codes()

#For a preview of what is possible
ConsolePrint.terminal_test()
```

<b>Preset string values may be used instead of the ANSI escape sequence for the format argument</b>
<table>
    <tr>
        <td>'default' =        '\033[0m'</td>
        <td>'grey' =           '\033[30m'</td>
        <td>'red' =            '\033[31m'</td>
    </tr>
    <tr>
        <td>'green' =          '\033[32m'</td>
        <td>'yellow' =         '\033[33m'</td>
        <td>'blue' =           '\033[34m'</td>
    </tr>
    <tr>
        <td>'magenta' =        '\033[35m'</td>
        <td>'cyan' =           '\033[36m'</td>
        <td>'white' =          '\033[37m'</td>
    </tr>
    <tr>
        <td>'bold' =           '\033[1m'</td>
        <td>'italics' =        '\033[3m'</td>
        <td>'underscore' =     '\033[4m'</td>
    </tr>
    <tr>
        <td>'strike' =         '\033[9m'</td>
        <td>'double_under' =   '\033[21m'</td>
        <td>'red_bg' =         '\033[41m'</td>
    </tr>
    <tr>
        <td>'green_bg' =       '\033[42m'</td>
        <td>'yellow_bg' =      '\033[43m'</td>
        <td>'blue_bg' =        '\033[44m'</td>
    </tr>
    <tr>
        <td>'magenta_bg' =     '\033[45m'</td>
        <td>'cyan_bg' =        '\033[46m'</td>
        <td>'white_bg' =       '\033[47m'</td>
    </tr>
</table>

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

<!-- 3.  This adds loading animations to terminal program.  The load time argument is specified as an integer in seconds.
```python
import ConsolePrint.loading as load  

load.countdown(5)
load.loading1(10)
print()
load.loading2(5)
print()
load.loading3(5)
``` -->
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
