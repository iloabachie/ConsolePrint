# ConsolePrint
This module making printing to the terminal more exciting by animating the text output.
You can also save routine console output to a file using the console2file module.
Created using python 3.11

# Installation
You may install it form PyPI.org using the pip command.
pip install ConsolePrint

# Usage
Copy the code below and run it from your IDE, preferable Visual Studio Code.  May not produce the desired output with IDLE.
You may change the arguments as desired

import ConsolePrint.animate as prt       
import ConsolePrint.console2file as file  
import ConsolePrint.loading as load        

# Test Cases
file.startConsoleSave()
'Saves all output between the start and end functions to file.'
from calendar import calendar
print(calendar(2023))
file.endConsoleSave()

prt.printing("hello this should print letter by letter", delay=0.05, style="letter", new_line=True, rev=False)
prt.printing("hello this should print word by word but in reverse", delay=0.05, style="word", new_line=True, rev=True)
prt.flashprint("The entire text should flash", flashes=5, delay=0.2, stay=True)
prt.flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2)
prt.animate1("This text is animated with #", symbol="#")
prt.animate2("Prints letter by letter but masked with # first", symbol="#", delay=0.05)
prt.text_box("M O N E Y  M A K E R", symbol="$", padding=True, wall=True)
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
