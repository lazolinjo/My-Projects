from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


while 1:
    if pyautogui.locateOnScreen('C:\Users\Andricka\Desktop\PythonBot\stickman.png') != None: #tries to locate the stickman.png on screen
        print('I can see it')
        time.sleep(0.5)
    else:
        print('I am unable to see it')
        time.sleep(0.5)