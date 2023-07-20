from pyautogui import *
import time
import keyboard
import pyautogui
import _thread
import time

from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

"""# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press  release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing  releasing
# twice on Mac OSX
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)"""



time.sleep(5)

def click():
    print("click")
    mouse.press(Button.left) 
    time.sleep(0.5) 
    mouse.release(Button.left)

number59 = pyautogui.locateCenterOnScreen('number59.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)   

number58 = pyautogui.locateCenterOnScreen('number58.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)    

number57 = pyautogui.locateCenterOnScreen('number57.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number56 = pyautogui.locateCenterOnScreen('number56.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)   

number55 = pyautogui.locateCenterOnScreen('number55.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number54 = pyautogui.locateCenterOnScreen('number54.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number53 = pyautogui.locateCenterOnScreen('number53.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number52 = pyautogui.locateCenterOnScreen('number52.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number51 = pyautogui.locateCenterOnScreen('number51.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number50 = pyautogui.locateCenterOnScreen('number50.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number49 = pyautogui.locateCenterOnScreen('number49.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number48 = pyautogui.locateCenterOnScreen('number48.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number47 = pyautogui.locateCenterOnScreen('number47.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number46 = pyautogui.locateCenterOnScreen('number46.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number45 = pyautogui.locateCenterOnScreen('number45.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number44 = pyautogui.locateCenterOnScreen('number44.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number43 = pyautogui.locateCenterOnScreen('number43.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number42 = pyautogui.locateCenterOnScreen('number42.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number41 = pyautogui.locateCenterOnScreen('number41.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

number40 = pyautogui.locateCenterOnScreen('number40.png', region=(0, 0, 1920, 1080), grayscale=False, confidence=0.90)
time.sleep(0.5)

while not keyboard.is_pressed('esc'):
    
    if number40 is not None:
        print("number40")
    if number41 is not None:
        print("number41")
    if number42 is not None:
        print("number42")
    if number43 is not None:
        print("number43")
    if number44 is not None:
        print("number44")
    if number45 is not None:
        print("number45")
    if number46 is not None:
        print("number46")
    if number47 is not None:
        print("number47")
    if number48 is not None:
        print("number48")
    if number49 is not None:
        print("number49")
    if number50 is not None:
        print("number50")
    if number51 is not None:
        print("number51")
    if number52 is not None:
        print("number52")
    if number53 is not None:
        print("number53")
    if number54 is not None:
        print("number54")
    if number55 is not None:
        print("number55")
    if number56 is not None:
        print("number56")
    if number57 is not None:
        print("number57")
    if number58 is not None:
        print("number58")
    if number59 is not None:
        print("number59")