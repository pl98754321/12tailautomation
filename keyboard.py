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

def useskill(skillname,skillnum,wait=True,contime=2):
    screen_check(skillname)
    click(skillnum)
    if wait:
        time.sleep(contime)

def screen_check(name,percent = 0.9):
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) != None:
            print("---- " + name + " complete----")
            break

def gotomission(mission):
    screen_check(mission)
    if mission == "905":
        screen_check("createdes800600")
        pg.click(1281,412) #ปุ่มสร้างแตกต่าง
    else :
        screen_check("create800600")
        pg.click(1216,415) #click create
    screen_check("start800600")
    pg.click(1216,415) #click start

#-------------------------------905----------------------------

def skipshadowboss():
    screen_check("shadowgod")
    while pg.locateOnScreen(filelocate("shadowgod"), confidence=0.9) != None:
        pg.click(847,321)

def run905mol():
    useskill("autogyrogun","1")
    click("e",distance=2)
    click(Key.tab)
    click("2")
    click(Key.tab)
    time.sleep(4.5)
    useskill("Reload","7",wait=False)
    useskill("autogyrogun","1")
    useskill("Syncomole","6",wait=False)
    click("w",distance=2)
    useskill("autogyrogun","1")
    click("q",distance=2)
    click(Key.tab)
    click("3")
    click(Key.tab)

def run905chm():
    screen_check("bloodbrun")
    click("z",distance=0.3)
    click("s",distance=4)
    click("1")
    time.sleep(0.75)
    click("2")
    time.sleep(4)
    #screen_check("bloodbrun")
    #click("1")
    #time.sleep(0.75)
    click("3")


#--------------------------------------------------------------------
def runwhilemine(mission,skillcheck = "autogyrogun",y=330):
    screen_check(skillcheck)
    click("q",distance=2)
    click("w",distance=0.5)
    for i in [800,880,950,1000,1080]:
        pg.click(i,y)
    gotomission(mission)

def runwhiledes(mission,skillcheck = "autogyrogun"):
    screen_check(skillcheck)
    time.sleep(1)
    click("q",distance=1.44)
    click("w",distance=0.42)
    for i in [825,855,873,903,933,963,993,1023,1053,1083]:
        pg.click(i,329)
    gotomission(mission)

def runwhileguild(mission,skillcheck = "autogyrogun"):
    screen_check("Firsttailguild")
    screen_check(skillcheck)
    click("s",distance=1.5)
    click("q",distance=1)
    time.sleep(1)
    pg.click(774,341)
    gotomission(mission)

#---------------------------------904-------------------------------------------------

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
    click("q",distance=1.7)
    click("w",distance=0.85)
    useskill("buildbot","9",contime=4)
    useskill("autogyrogun","1")
    click("e",distance=3.4)
    useskill("autogyrogun","1")
    click(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    useskill("reload","7",wait=False)
    click("w",distance=2)
    useskill("autogyrogun","1")
    click("q",distance=3)
    click("w")
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)
    click("q",distance=1)

#----------------------------------------------------------------------------
def pausewhiledrop(name):
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

def collectrewarditem():
    screen_check("postbutton")
    for i in [740,770,800,830,860,890,920]:
        pg.click(i,340)
        time.sleep(1)

def takescreenshot():
    path = r"C:\Users\plem67\Desktop\New folder (2)\screenshot\\"
    savetime = time.localtime()
    screen_check("postbutton")
    screen_check('MissionCamp')
    screenshot_raw = pg.screenshot()
    screenshot_raw.save(path + "604" + str(savetime.tm_mday) + str(savetime.tm_hour) + str(savetime.tm_min) + str(savetime.tm_sec) +r".PNG")
    print("##### take screenshot " + time.ctime() + " #########")

def gocamp():
    screen_check('postbutton')
    screen_check('MissionCamp')
    time.sleep(1)
    pg.click(890,484)
#----------------------------------------------------------------------------
keyboard = Controller()
#pausewhiledrop("test")
#print("dada")
while True:
    run604()
    pausewhiledrop("cannon")
    takescreenshot()
    gocamp()
    runwhiledes("604")