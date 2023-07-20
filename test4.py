from pyautogui import *
import keyboard
import pyautogui
import time
from datetime import datetime
from pynput.mouse import Button, Controller

mouse = Controller()
count =0

def number50():
    count =0
    number50 = pyautogui.locateCenterOnScreen('number50.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
    if number50 is not None:
        print("number50")
        count = count +1
        now = datetime.now()
        timestamp = datetime.timestamp(now)

    if number50 is not None and count == 2:
        print("number50 count2")
        now2 = datetime.now()
        timestamp2 = datetime.timestamp(now)
        timefinal = timestamp2 - timestamp
        if timefinal < 60:
            print("beuuuuh")
   


#si count = 3 -> notif push
#on verifie les diff timestamp


while not keyboard.is_pressed('esc'):
    number50()
    
    