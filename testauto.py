from functools import cmp_to_key
from sys import flags
from pynput.keyboard import Key, Controller
import pyautogui as pg
import time

def filelocate(name):
    path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
    return path + name + r".png"

def click(typekey,distance = 0.1):
    keyboard.press(typekey)
    time.sleep(distance)
    keyboard.release(typekey)

def useskill(skillname,skillnum,wait=True,contime=1.5):
    screen_check(skillname)
    click(skillnum)
    if wait:
        time.sleep(contime)

def screen_check(name,percent = 0.9):
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) != None:
            print("---- " + name + " complete----")
            break

def gotomission(mission,wait_gomission=False):
    screen_check(mission)
    if mission == "905":
        screen_check("createdes800600")
        pg.click(1281,412) #ปุ่มสร้างแตกต่าง
    else :
        screen_check("create800600")
        pg.click(1216,415) #click create
    if wait_gomission:
        screen_check("keystart")
    screen_check("start800600")
    pg.click(1216,415) #click start

keyboard = Controller()
time.sleep(0.5)
def collecrewarditemByImg(name):
    while pg.locateOnScreen(filelocate(name),confidence=0.9,region=(725,330,225,100)):
        x,y = pg.locateCenterOnScreen(filelocate(name),confidence=0.9,region=(725,330,225,100))
        pg.click(x, y)
        time.sleep(0.7)