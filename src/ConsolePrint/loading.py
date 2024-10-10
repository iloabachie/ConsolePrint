import time
import os

print('\033[0m', end="\r")
__terminal_width = os.get_terminal_size().columns

def countdown(t, confirm=True):
    '''Enter countdown time in seconds'''
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")        
        time.sleep(1)
        t -= 1
    if confirm:
        print('Timer completed!')

def loading1(t, text='Loading...', confirm=True):
    t = 20 if t > 15 else 15 if t > 10 else 10
    x = t
    if __terminal_width < 70 + len(text):
        loading3(max(15, t))
    else:
        percent = 0
        for _ in range(t):        
            percent += 100 / x
            y = round(percent, 1) / 100
            print(f" {text} [{'|||' * _}{'   ' * (x - _ - 1)}]", '{:4.0%}'.format(y), end="\r")
            time.sleep(0.2)
            t -= 1    
    if confirm:
        print(f'\n {text.strip('.')} complete!')

def loading2(t, text='Loading...', confirm=False):
    "Takes two arguments, time and text to display such as 'loading...'"
    load = ['-', '\\', '|', '/', ] * t
    for _ in load:
        print(f"  {_}  {text}", end='\r')
        time.sleep(0.5)
    if confirm:
        print('\nLoading complete!   ')
    
def loading3(t):
    the_bar = "     ======     "
    nums = ([*range(len(the_bar)-5)] + [*range(len(the_bar) - 7, 0, -1)]) * t
    for i, a in enumerate(nums):
        print(f' [{the_bar[a:a + 6]}]', end='\r')
        time.sleep(0.2) 
        if i >= t // 0.2:
            break
    if __name__ == '__main__':
        print('\nLoading Complete!')


if __name__ == '__main__':    
    countdown(5)
    print()
    loading1(15, 'Processing...')  
    print()
    loading2(5, 'Processing request...')
    print()
    loading3(5)
    
   