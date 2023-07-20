from pyautogui import *
import time
import keyboard
import pyautogui

from pynput.mouse import Button, Controller

mouse = Controller()

def click():
    print("click")
    mouse.press(Button.left) 
    time.sleep(0.5) 
    mouse.release(Button.left)

def refresh():
    print("recherche fenetre")
    fenetre = pyautogui.locateCenterOnScreen('fenetre.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.90)
    if fenetre is not None:
        print("fenetre trouvé")
        mouse.position = (fenetre)  
        click()
        pyautogui.hotkey('ctrl', 'F5')

refresh()