import pyautogui
import os
from time import sleep
import time
import sys



def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "#"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)


for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(0.1) # any code you need

pyautogui.hotkey('ctrl', 'alt', 't')

sleep(0.5)

pyautogui.write('echo -- Welcome to the underworld --  ')

pyautogui.press('enter')



sleep(2)



pyautogui.write('cmatrix')


pyautogui.press('enter')

sleep(0)

pyautogui.hotkey('f11')
