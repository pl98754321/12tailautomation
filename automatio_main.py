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

#-------------------------------905----------------------------

def skipshadowboss():
    screen_check("shadowgod")
    while pg.locateOnScreen(filelocate("shadowgod"), confidence=0.9) != None:
        pg.click(847,321)

#--------------------------------------------------------------------
def runwhilecamp(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    time.sleep(1)
    click("q",distance=1.66)
    click("w",distance=0.45)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecampsnow(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    time.sleep(1)
    click("s",distance=1.5)
    click("q",distance=1.4)
    time.sleep(1)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhileguild(mission,skillcheck = "autogyrogun"):
    screen_check("Firsttailguild")
    screen_check(skillcheck)
    click("s",distance=1.5)
    click("q",distance=1)
    time.sleep(1)
    pg.click(774,341)
    gotomission(mission)

#---------------------------------904-------------------------------------------------
def run905mol():
    useskill("autogyrogun","1")
    #----------
    click("e",distance=2)
    useskill("buildbot","9",contime=3.5)
    useskill("Reload","7",wait=False)
    useskill("autogyrogun","1")
    useskill("Syncomole","6",wait=False)
    #----------
    click("w",distance=2)
    useskill("autogyrogun","1")
    #----------
    click("q",distance=2)

def run905chm():
    screen_check("bloodbrun")
    click("z",distance=0.3)
    click("s",distance=4)
    click("1")
    time.sleep(0.75)
    click("2")
    time.sleep(4)
    click("3")

def run904():
    screen_check("autogyrogun")
    click("c",distance=2.3)
    time.sleep(1)
    click("w",distance=10)
    click("s")
    useskill("autogyrogun","1")
    click("w",distance=1.5)

def run604():
    useskill("autogyrogun","1")
    #----------
    click("q",distance=1.7)
    click("w",distance=0.85)
    useskill("buildbot","9",contime=4)
    useskill("autogyrogun","1")
    #----------
    click("e",distance=3.4)
    useskill("autogyrogun","1")
    click(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    useskill("reload","7",wait=False)
    #----------
    click("w",distance=2)
    useskill("autogyrogun","1")
    #----------
    click("q",distance=3)
    click("w")
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)
    click("q",distance=1)

def run403():
    screen_check("autogyrogun")
    click("w")
    useskill("autogyrogun","1")
    useskill("buildbot","9",contime=3.5)
    #----------
    click("s",distance=3.5)
    click("q",distance=3)
    useskill("autogyrogun","1")
    #----------
    click("e",distance=3)
    click("s",distance=2)
    click("e",distance=3)
    useskill("autogyrogun","1")
    click(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    #----------
    click("q",distance=1.5)
    click("s")
    useskill("autogyrogun","1")
    #----------
    click("q",distance=1.5)
    useskill("reload","7",wait=False)
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)

#----------------------------------------------------------------------------
def pausewhiledropF4(name):
    click(Key.f4)
    time.sleep(1)
    pg.moveTo(1280,107)
    pg.click(1280,107)
    pg.click(1280,107)
    while pg.locateOnScreen(filelocate("postbutton"),confidence=0.9) == None:
        if pg.locateOnScreen(filelocate(name),confidence=0.7) != None:
            print("have " + name)
            while True:
                print("!!!!!!!!!!!!!!!!!!!! colllect " + name)
                time.sleep(5)
    print("!!!donthave " + name)

def pausewhiledrop(name):
    screen_check("postbutton")
    for i in range(5):
        if pg.locateOnScreen(filelocate(name),confidence=0.7) != None:
            while True:
                print("!!!!!!!!!!!!!!!!!!!! colllect " + name)
                time.sleep(5)
        print("donthave " + name + " " + str(i))
        time.sleep(0.5)

def collectrewarditem():
    screen_check("postbutton")
    for i in [740,770,800,830,860,890,920]:
        if pg.locateOnScreen(filelocate("postbutton"),confidence=0.9) == None:
            break
        pg.click(i,350)
        time.sleep(1)

def takescreenshot(name):
    path = r"C:\Users\plem67\Desktop\New folder (2)\screenshot\\"
    savetime = time.localtime()
    subfixname = "_" + str(savetime.tm_mday) + "_" + str(savetime.tm_hour) + "-" + str(savetime.tm_min)
    screen_check("postbutton")
    screen_check('MissionCamp')
    screenshotraw_raw = pg.screenshot()
    screenshotraw_raw.save(path + r"raw\\" + name + subfixname +r".PNG")
    screenshot_raw = pg.screenshot(region=(569,24,800,600))
    screenshot_raw.save(path + name + subfixname +r".PNG")
    print("##### take screenshot " + time.ctime() + " #########")

def gocamp():
    screen_check('postbutton')
    screen_check('MissionCamp')
    time.sleep(1)
    pg.click(890,484)

#----------------------------------------------------------------------------

def allin604():
    run604()
    pausewhiledropF4("cannon")
    pausewhiledrop("pumkincannon")
    takescreenshot("604")
    gocamp()
    runwhilecamp("604")

def allin905mol():
    skipshadowboss()
    run905mol()
    collectrewarditem()
    gocamp()
    runwhilecamp("905")

def allin403():
    run403()
    gocamp()
    runwhilecampsnow("403",wait_runwhile=True)



#----------------------------------------------------------------------------
keyboard = Controller()
time.sleep(0.5)
while True:
    allin403()