"""This module  saves terminal output to file."""
import sys
import subprocess
from loading import loading2

def startConsoleSave():
    """Starts the process to save the output to file"""
    global filename
    filename = input("Enter the output filename and extension: ") # specified filename/path      
    sys.stdout = open(filename, 'a')  # redirects output to specified file


def endConsoleSave():  
    """Ends the save to file process and returns output to console"""  
    sys.stdout.close()
    sys.stdout = sys.__stdout__   # redirects output from file back to terminal
    loading2(1, "")
    print("    ")
    print(f"Output has been saved to {filename}")
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
    
    startConsoleSave()
    
    print("Printing Calendar")
    print(calendar.calendar(2023))
    
    endConsoleSave()    
