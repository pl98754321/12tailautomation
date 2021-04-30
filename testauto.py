from pynput import keyboard
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

def useskill(skillname,skillnum,wait=True):
    screen_check(skillname)
    click(skillnum)
    if wait:
        time.sleep(3.5)

def screen_check(name,percent = 0.9):
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) != None:
            print("---- " + name + " complete----")
            break

def gotomission(mission):
    screen_check("autogyrogun")
    click("q",distance=2)
    click("w",distance=0.5)
    for i in [800,880,950,1000]:
        pg.click(i,330)
    screen_check("905800600")
    screen_check("createdes800600")
    pg.click(1281,412) #click create
    screen_check("start800600")
    pg.click(1216,415) #click start

def pausewhiledrop(name):
    click(Key.f4)
    time.sleep(1)
    pg.click(1280,115)
    while pg.locateOnScreen(filelocate("postbutton"),confidence=0.9) == None:
        if pg.locateOnScreen(filelocate(name),confidence=0.7) != None:
            print("have " + name)
            while True:
                print("!!!!!!!!!!!!!!!!!!!! colllect " + name)
                time.sleep(5)
    print("!!!donthave " + name)

time.sleep(0.1)
keyboard=Controller()
path = r"C:\Users\plem67\Desktop\New folder (2)\screenshot\\"
savetime = time.localtime()
screenshot_raw = pg.screenshot(region=(569,24,800,600))
screenshot_raw.save(path + "604" + str(savetime.tm_mday) + str(savetime.tm_hour) + str(savetime.tm_min) + str(savetime.tm_sec) +r".PNG")
