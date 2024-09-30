"""This module  saves terminal output to file."""
import sys
import os
import subprocess
import time
from functools import wraps


def __saving(t, text='Writing to file...', confirm=False):
    "Takes two arguments, time and text to display such as 'loading...'"
    load = ['-', '\\', '|', '/', '-'] * t
    print()
    for _ in load:
        print(f"  {_}  {text}", end='\r')
        time.sleep(0.4)
    if confirm:
        print('Complete!!!             ')
        
def __open_file(filename, prompt:bool=False):    
    if prompt:
        if 'linux' in sys.platform:
            print("Prompt only works with Windows OS")
        else:
            open_file = input("\nWould you like to open the file? Y/n: ").lower().strip()
            while open_file not in ['y', 'yes', 'no', 'n', '']:
                open_file = input("\nInvalid input. Would you like to open the file? Y/n: ").lower().strip()
            if open_file in ['y', 'yes', '']:
                try:
                    subprocess.Popen(["start", "", f'{filename}.txt'], shell=True)
                except FileNotFoundError:
                    print("File not found.")
                except OSError:
                    print("Error opening file.")
                else:
                    print("File opened in OS Window")    

def startConsoleSave(name:str='code_output'):
    """Starts the process to save the output to file"""
    global filename
    filename = name 
    sys.stdout = open(f'{filename}.txt', 'a')  # redirects output to specified file


def endConsoleSave(prompt=False):  
    """Ends the save to file process and returns output to console"""  
    sys.stdout.close()
    sys.stdout = sys.__stdout__   # redirects output from file back to terminal
    __saving(1)
    if 'linux' in sys.platform:
        print(f"Output has been saved to \033[36m{os.getcwd()}/{filename}.txt\033[0m")
    else:
        print(f"Output has been saved to \033[36m{os.getcwd()}\\{filename}.txt\033[0m")
    __open_file(filename, prompt)


def func2file(filename:str='function_output', prompt:bool=False):
    '''Writes the output of a function to a text file'''
    def decorator(funct):
        @wraps(funct)
        def wrapper(*args, **kwargs):
            with open(f"{filename}.txt", 'a') as sys.stdout:
                print('Function logs:\n')
                output = funct(*args, **kwargs)
                if output:
                    print(f'\nReturn value for {funct.__name__} >> ', output)
            sys.stdout = sys.__stdout__
            __saving(1)
            if 'linux' in sys.platform:
                print(f"Logs and function return value have been saved to \033[36m{os.getcwd()}/{filename}.txt\033[0m")
            else:
                print(f"Logs and function return value have been saved to \033[36m{os.getcwd()}\\{filename}.txt\033[0m") 
            __open_file(filename, prompt)
        return wrapper
    return decorator


if __name__ == "__main__":
    print("*****\nRunning module test")
    import calendar, random
    
    startConsoleSave('bbb')
    print("Printing Calendar")
    print(calendar.calendar(random.randint(1900, 2199)))    
    endConsoleSave()      

    @func2file(filename='aaa', prompt=True)
    def cal_print():
        '''Calendar print'''
        print("Printing Calendar")
        print(calendar.calendar(random.randint(1900, 2199)))
        return "######"
    
    cal_print()    
    print("End of Test\n*****")