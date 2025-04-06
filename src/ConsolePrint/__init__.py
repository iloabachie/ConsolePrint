from .ansi import ansi_codes
from .animate import terminal_test
from .logo import version

print('\033[0m', end="\r")

__pkg__ = 'ConsolePrint'
__version__ = version