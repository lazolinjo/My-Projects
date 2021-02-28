#Ovo je piano tiles python bot, napravljen 17.2.2021/Lazar Andrejic
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#definise klik
def click(x,y):
    win32api.setCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #brzina klika
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Zaustavlja bota na klik 'q' na tast
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(581,400)[0] == 0:
        click(581,400)
    if pyautogui.pixel(682,400)[0] == 0:
        click(682,400)
    if pyautogui.pixel(770,400)[0] == 0:
        click(770,400)
    if pyautogui.pixel(869,400)[0] == 0:
        click(869,400)