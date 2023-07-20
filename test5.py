from pyautogui import *
import keyboard
import pyautogui
import time
from datetime import datetime
from pynput.mouse import Button, Controller

mouse = Controller()

def number50():
    number50 = pyautogui.locateCenterOnScreen('number50.png', region=(496, 472, 309, 156), grayscale=False, confidence=0.90)
    if number50 is not None:
        print("number50")
       
        

#si count = 3 -> notif push
#on verifie les diff timestamp


while not keyboard.is_pressed('esc'):
    number50()
    
    