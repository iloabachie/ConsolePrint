import os
if os.getenv('ENV') == 'development':
    from ansi import ansi_codes
    from animate import terminal_test
    from logo import version
else:
    from .ansi import ansi_codes
    from .animate import terminal_test
    from .logo import version


print('\033[0m', end="\r")


__title__ = 'ConsolePrint'
__version__ = version
__license__ = 'MIT'
__author__ = 'Udemezue Iloabachie'
__contact__ = 'udemezue@gmail.com'
__url__ = 'https://github.com/iloabachie/ConsolePrint'
__description__ = 'Add animation and color to the output or save the output to a text file'
