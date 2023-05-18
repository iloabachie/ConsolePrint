# Code test
# animate.py
if __name__ == "__main__":
    printing("This text prints word by word. Cool isn't it?", style='word', delay=0.3)
    printing("This text prints letter by letter and does not move to the new line", 0.06, 'letter', False, False)
    print()
    printing("This text prints letter by letter but in reverse", rev=True)
    flashprint("This entire Text is flashing")
    flashtext('The word at the end of this text is ', 'flashing', delay=0.2, blinks=5)
    animate1("This text is animated with # symbol")
    animate2("This text is animated with # symbol")              
    star_square(8, symbol="&")    
    text_box("C O D E  B R E A K E R", symbol="=", padding=True, wall=False)

# console2file.pt
if __name__ == "__main__":
    print("Running module test")
    import calendar
    
    startConsoleSave()
    
    print("Printing Calendar")
    print(calendar.calendar(2023))
    
    endConsoleSave()  

# loading.py
if __name__ == '__main__':
    countdown(5)
    print()
    loading1(20)  
    print()
    loading2(5, 'thinking...')
    print()
    loading3(5)