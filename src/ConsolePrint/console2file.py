"""This module  saves terminal output to file."""
import sys
import subprocess
import time


def __saving(t, text='Writing to file...', confirm=False):
    "Takes two arguments, time and text to display such as 'loading...'"
    load = ['-', '\\', '|', '/', '-'] * t
    print()
    for _ in load:
        print(f"  {_}  {text}", end='\r')
        time.sleep(0.4)
    if confirm:
        print('Complete!!!             ')
        
def __open_file(filename, prompt:bool=True):
    if 'linux' in sys.platform:
        prompt = False
        print("Prompt only works with Windows OS")
    if prompt:
        open_file = input("\nWould you like to open the file? y/n: ")
        if open_file.strip().lower() == "y":
            try:
                subprocess.Popen(["start", "", filename], shell=True)
            except FileNotFoundError:
                print("File not found.")
            except OSError:
                print("Error opening file.")
    

def startConsoleSave(name:str='code_output'):
    """Starts the process to save the output to file"""
    global filename
    filename = name 
    sys.stdout = open(f'{filename}.txt', 'a')  # redirects output to specified file


def endConsoleSave(prompt=True):  
    """Ends the save to file process and returns output to console"""  
    sys.stdout.close()
    sys.stdout = sys.__stdout__   # redirects output from file back to terminal
    __saving(1)
    print(f"Output has been saved to \033[36m{filename}.txt\033[0m")
    __open_file(filename, prompt)


def func2file(filename:str='function_output', prompt:bool=True):
    '''Writes the output of a function to a text file'''
    def decorator(funct):
        def wrapper(*args, **kwargs):
            with open(f"{filename}.txt", 'a') as sys.stdout:
                output = funct(*args, **kwargs)
                print('\nThe function return value is:')
                print('>> ', output)
            sys.stdout = sys.__stdout__
            __saving(1)
            print(f"Logs and function return value have been saved to \033[36m{filename}.txt\033[0m") 
            __open_file(filename, prompt)
        return wrapper
    return decorator
        
    

if __name__ == "__main__":
    print("Running module test\n*****")
    import calendar, random
    
    startConsoleSave('bbb')
    print("Printing Calendar")
    print(calendar.calendar(random.randint(1900, 2199)))    
    endConsoleSave()      

    @func2file('aaa', prompt=True)
    def prints():
        print("Printing Calendar")
        print(calendar.calendar(random.randint(1900, 2199)))
        return "my output"
    
    prints()
    
    print("*****\nEnd of Test")