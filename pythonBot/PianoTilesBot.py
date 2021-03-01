from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Defines the click function
def click(x,y):
    win32api.setCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #brzina klika
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Stops bot with "Q" on keyboard
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(581,400)[0] == 0:
        click(581,400)
    if pyautogui.pixel(682,400)[0] == 0:
        click(682,400)
    if pyautogui.pixel(770,400)[0] == 0:
        click(770,400)
    if pyautogui.pixel(869,400)[0] == 0:
        click(869,400)