import pandas as pd
from openpyxl import load_workbook
from array import array
from pyautogui import *
import keyboard
import pyautogui
import pygsheets
from datetime import datetime
import time
from pynput.mouse import Button, Controller
import http.client, urllib

'''mouse = Controller()'''
global notif
global alertepush
tabTime = []
tabFinal = []
alertepush = 0

def push_over(param):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    message = "Alerte Binance " + str(param) + " fois 0 en " + str(param - 1) + "minute"
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": "asgje1g4cman6vpqrnj5y1b9gcktqn",
                     "user": "uQhfbyotatsy7zNPahVspzzDz3vFpg",
                     "message": message,
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

def wait_sec(param, number):
    while number == "None":
        number = pyautogui.locateCenterOnScreen(param, region=(0, 0, 2560, 1440), grayscale=False,
                                                     confidence=0.97)
        if number is not None:
            return param


while not keyboard.is_pressed('esc'):

    minute = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29,
              28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    startnumber = None
    number = None
    index = 0
    time = time
    start = None

    print('========> Synchronisation en cours <========')
    while startnumber is None:
        print('========> Analyse en cours <========')
        startnumber = pyautogui.locateCenterOnScreen('binance51.png', region=(0, 0, 2560, 1440), grayscale=False,
                                                     confidence=0.97)

    if startnumber is not None:
        print('binance51')

        for seconde in minute:
            index += 1
            image = 'binance' + str(seconde) + '.png'
            number = None
            statut = 0
            startRef = time.time()
            autobreak = 0


            while statut == 0:
                start = time.time()
                local_time = time.ctime(start)
                if start <= startRef + 2 :
                    number = pyautogui.locateCenterOnScreen(image, region=(0, 0, 2560, 1440), grayscale=False,
                                                            confidence=0.97)
                    if number is not None:
                        print("========> Analyse numero : " + str(seconde) + " <========")
                        statut = 1

                else:
                    statut = 1
                    autobreak = 1
                    notif = [(seconde - 1), local_time]
                    print('========> Fin du decompte : ' + str(seconde - 1) + '<========')

            if autobreak == 1 or seconde == 0:
                tabTime.append(notif)
                print('========> Push office <========')
                push_googleshet(tabTime)
                if seconde == 0:
                    alertepush += 1

                else:
                    alertepush = 0

                if alertepush >= 2:
                    push_over(alertepush)
                    print('========> Alerte PushOver <========')

                print('========> Reinitialisation <========')
                break











