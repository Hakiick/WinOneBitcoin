import pandas as pd
'''from openpyxl import load_workbook'''
from array import array
from pyautogui import *
import keyboard
import pyautogui
'''import pygsheets'''
from datetime import datetime
import time
from pynput.mouse import Button, Controller
import http.client, urllib

'''mouse = Controller()'''
tabTime = []
tabFinal = []

def push_over():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": "asgje1g4cman6vpqrnj5y1b9gcktqn",
                     "user": "uQhfbyotatsy7zNPahVspzzDz3vFpg",
                     "message": "Alerte Binance",
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

def push_googleshet(tabTime):
    writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
    writer.book = load_workbook('demo.xlsx')
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(r'demo.xlsx')
    tF = pd.DataFrame(data=tabTime)
    tF.to_excel(writer, index=False, header=False, startrow=len(reader) + 1)
    writer.close()
    print(tabTime)






'''def number():
    count = 0
    while count < 22:
        number40 = pyautogui.locateCenterOnScreen('binance.png', region=(0, 0, 2560, 1440), grayscale=False, confidence=0.97)

        for seconde in range(0, 2):
            print(seconde)

        if number40 is not None:
            print("number40")
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            tabTime.append(timestamp)
            count = count + 1
            time.sleep(0.8)
            print(count)
            number39 = pyautogui.locateCenterOnScreen('binance39.png', region=(0, 0, 2560, 1440), grayscale=False,
                                                      confidence=0.97)

            if number39 is not None:
                print("number39")
                now = datetime.now()
                timestamp = datetime.timestamp(now)
                tabTime.append(timestamp)
                count = count + 1
                time.sleep(0.8)

                number36 = pyautogui.locateCenterOnScreen('binance38.png', region=(0, 0, 2560, 1440), grayscale=False,
                                                          confidence=0.97)
                if number36 is not None:
                    print("number38")
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    tabTime.append(timestamp)
                    count = count + 1

            if count == 20:
 
'''

def wait_sec(param, number):
    while number == "None":
        number = pyautogui.locateCenterOnScreen(param, region=(0, 0, 2560, 1440), grayscale=False,
                                                     confidence=0.97)
        if number is not None:
            return param


while not keyboard.is_pressed('esc'):

    minute = [55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29,
              28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    startnumber = "None"
    number = "None"
    index = 0

    while startnumber == "None":
        startnumber = pyautogui.locateCenterOnScreen('binance56.png', region=(0, 0, 2560, 1440), grayscale=False,
                                                     confidence=0.90)
        print('analyse')


    if startnumber is not None:
        print('binance56')

        for seconde in minute:
            index += 1
            image = 'binance' + str(seconde) + '.png'
            print('trololo' + str(index))
            number = "None"

            while number == "None":
                number = pyautogui.locateCenterOnScreen(image, region=(0, 0, 2560, 1440), grayscale=False,
                                                        confidence=0.97)
                print(seconde)
                print(number)

            if number is not None:
                print("number" + str(seconde))






