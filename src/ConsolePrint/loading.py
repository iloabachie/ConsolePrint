import time

def countdown(t, confirm=True):
    '''Enter countdown time in seconds'''
    # t = int(input('Enter time in secs: '))
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")        
        time.sleep(1)
        t -= 1
    if confirm:
        print('Timer completed!')

def loading1(t, confirm=True):
    x = t
    percent = 0
    for _ in range(t):        
        percent += 100 / x
        y = round(percent, 1) / 100
        print(f" Loading... [{'|||' * _}{'   ' * (x - _ - 1)}]", '{:4.0%}'.format(y), end="\r")
        time.sleep(0.2)
        t -= 1    
    if confirm:
        print('\n Loading complete!')

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
    for a in nums:
        print(f' [{the_bar[a:a + 6]}]', end='\r')
        time.sleep(0.2) 
    if __name__ == '__main__':
        print('\nLoading Complete!')


if __name__ == '__main__':
    countdown(5)
    print()
    loading1(20)  
    print()
    loading2(5, 'thinking...')
    print()
    loading3(5)
  

   