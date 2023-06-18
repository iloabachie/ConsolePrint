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

def startConsoleSave(name:str=''):
    """Starts the process to save the output to file"""
    global filename
    if name:
        filename = name
    else:
        filename = 'terminal_output.txt'    
    sys.stdout = open(filename, 'a')  # redirects output to specified file


def endConsoleSave(prompt=True):  
    """Ends the save to file process and returns output to console"""  
    sys.stdout.close()
    sys.stdout = sys.__stdout__   # redirects output from file back to terminal
    __saving(1, confirm=True)
    print(f"Output has been saved to \033[36m{filename}\033[0m")
    if prompt:
        open_file = input("\nWould you like to open the file? y/n: ")
        if open_file.strip().lower() == "y":
            try:
                subprocess.Popen(["start", "", filename], shell=True)
            except FileNotFoundError:
                print("File not found.")
            except OSError:
                print("Error opening file.")


if __name__ == "__main__":
    print("Running module test")
    import calendar
    
    startConsoleSave() # Saves file to default terminal_output.txt 
    
    print("Printing Calendar")
    print(calendar.calendar(2023))
    
    endConsoleSave()    
