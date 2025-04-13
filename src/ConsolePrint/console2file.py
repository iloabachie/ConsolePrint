"""This module  saves terminal output to file."""
import sys
import os
import subprocess
import time
from functools import wraps


class SaveToFile:
    def __init__(self, name:str='output', prompt:bool=False):        
        self.name = name
        self.prompt = prompt

    def __saving(t, text='Writing to file...', confirm=False):
        "Takes two arguments, time and text to display such as 'loading...'"
        load = ['-', '\\', '|', '/', '-'] * t
        print()
        for _ in load:
            print(f"  {_}  {text}", end='\r')
            time.sleep(0.3)
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

    @staticmethod
    def startConsoleSave(name:str='output'):
        """Starts the process to save the output to file"""
        global filename
        filename = name 
        sys.stdout = open(f'{filename}.txt', 'a')

    @staticmethod
    def endConsoleSave(prompt=False):  
        """Ends the save to file process and returns output to console"""  
        sys.stdout.close()
        sys.stdout = sys.__stdout__ 
        SaveToFile.__saving(1)
        if 'linux' in sys.platform:
            print(f"Output has been saved to \033[36m{os.getcwd()}/{filename}.txt\033[0m")
        else:
            print(f"Output has been saved to \033[36m{os.getcwd()}\\{filename}.txt\033[0m")
        SaveToFile.__open_file(filename, prompt)

    @staticmethod
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
                SaveToFile.__saving(1)
                if 'linux' in sys.platform:
                    print(f"Logs and function return output has been saved to \033[36m{os.getcwd()}/{filename}.txt\033[0m")
                else:
                    print(f"Logs and function return output has been saved to \033[36m{os.getcwd()}\\{filename}.txt\033[0m") 
                SaveToFile.__open_file(filename, prompt)
            return wrapper
        return decorator

    def __enter__(self):
        SaveToFile.startConsoleSave(self.name)        
    
    def __exit__(self, exc_type, exc_val, exc_tb):        
        if exc_type:
            sys.stdout = sys.__stdout__
            print('Error occurred', exc_type, exc_val, exc_tb, sep='\n')
        else:  
            SaveToFile.endConsoleSave(self.prompt)


func2file = SaveToFile.func2file
startConsoleSave = SaveToFile.startConsoleSave
endConsoleSave = SaveToFile.endConsoleSave


if __name__ == "__main__":
    print("*****\nModule test")
    from calendar import calendar
    
    startConsoleSave('first')
    print("log 1: Printing Calendar...")
    print(calendar(2025))
    print("log 2: Printing finished...")   
    endConsoleSave()      

    @func2file(filename='second', prompt=False)
    def cal_print():
        '''Calendar print'''
        print("log 1: Printing Calendar...")
        print(calendar(2025))
        print("log 2: Printing finished...")
        return "result"
    
    cal_print() 
    
    with SaveToFile(name='third'):        
        print("log 1: Printing Calendar...")
        print(calendar(2025))
        print("log 2: Printing finished...")  
        
    print("\nEnd of Test\n*****")
    