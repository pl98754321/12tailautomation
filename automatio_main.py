from functools import cmp_to_key
from sys import flags
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyautogui as pg
import time

#-------------------------------basic----------------------------

def filelocate(name):
    path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
    return path + name + r".png"

def press(typekey,distance = 0.1):
    keyboard.press(typekey)
    time.sleep(distance)
    keyboard.release(typekey)

def useskill(skillname,skillnum,wait=True,contime=0.75):
    screen_check(skillname)
    press(skillnum)
    if wait:
        time.sleep(contime)

def screen_check(name,percent = 0.9):
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) != None:
            print("---- " + name + " complete----")
            break

def holdimg(name,percent = 0.9,waittime=0):
    print("---- hold " + name + " ----")
    screen_check(name)
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) == None:
            print("---- hold " + name + " complete----")
            time.sleep(waittime)
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

def skip(name = "shadowgod"):
    screen_check(name)
    print(f"###### skip{name} process ######")
    while pg.locateOnScreen(filelocate(name), confidence=0.9) != None:
        pg.click(847,321)

def holdimg(name,percent = 0.9,waittime=0):
    print("---- hold " + name + " ----")
    screen_check(name)
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) == None:
            print("---- hold " + name + " complete----")
            time.sleep(waittime)
            break

#--------------------------------runwhilecamp------------------------------
def runwhilecamp(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    press("q",distance=1.5)
    press("w",distance=0.45)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecampchm(mission,skillcheck = "bloodbrun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    press("q",distance=2)
    press("w",distance=0.75)
    for i in range(790,1100,50):
        pg.click(i,385)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecamprab(mission,skillcheck = "gilshot",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    press("q",distance=2.3)
    press("w",distance=1)
    for i in range(790,1100,50):
        pg.click(i,340)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecampsnow(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecampsnow process ######")
    time.sleep(1)
    press("s",distance=1.5)
    press("q",distance=1.3)
    time.sleep(1)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhileguild(mission,skillcheck = "autogyrogun"):
    screen_check("Firsttailguild")
    screen_check(skillcheck)
    print("###### runwhileguild process ######")
    press("s",distance=1.5)
    press("q",distance=1)
    time.sleep(1)
    pg.click(774,341)
    gotomission(mission)

#-------------------------------postbattle----------------------------------------
def pausewhiledrop(name):
    screen_check("postbutton")
    for i in range(3):
        if pg.locateOnScreen(filelocate(name),confidence=0.7) != None:
            while True:
                print("!!!!!!!!!!!!!!!!!!!! colllect " + name)
                time.sleep(5)
        print("donthave " + name + " " + str(i+1))
        time.sleep(0.5)

def collecrewarditemByImg(name):
    screen_check("postbutton")
    while pg.locateOnScreen(filelocate(name),confidence=0.7,region=(725,330,225,100)) != None:
        x,y = pg.locateCenterOnScreen(filelocate(name),confidence=0.7,region=(725,330,225,100))
        pg.click(x, y)
        time.sleep(0.9)

def takescreenshot(name):
    path = r"C:\Users\plem67\Desktop\New folder (2)\screenshot\\"
    savetime = time.localtime()
    subfixname = "_" + str(savetime.tm_mday) + "_" + str(savetime.tm_hour) + "-" + str(savetime.tm_min)
    screen_check("postbutton")
    screen_check('MissionCamp')
    screenshot_raw = pg.screenshot(region=(569,24,800,600))
    screenshot_raw.save(path + name + r"\\" + name + subfixname)
    print("##### take screenshot " + time.ctime() + " #########")

def gocamp():
    screen_check('postbutton')
    screen_check('MissionCamp')
    time.sleep(0.25)
    pg.click(890,484)

#----------------------------------------------------------------------------

keyboard = Controller()
time.sleep(0.5)