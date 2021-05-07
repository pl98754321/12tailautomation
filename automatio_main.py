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

def useskill(skillname,skillnum,wait=True,contime=0.75):
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
    print("###### skipshadowboss process ######")
    while pg.locateOnScreen(filelocate("shadowgod"), confidence=0.9) != None:
        pg.click(847,321)

#--------------------------------------------------------------------
def runwhilecamp(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    click("q",distance=1.5)
    click("w",distance=0.45)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecampchm(mission,skillcheck = "bloodbrun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    click("q",distance=2)
    click("w",distance=0.75)
    for i in range(790,1100,50):
        pg.click(i,385)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecamprab(mission,skillcheck = "gilshot",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecamp process ######")
    time.sleep(0.2)
    click("q",distance=2.3)
    click("w",distance=1)
    for i in range(790,1100,50):
        pg.click(i,340)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhilecampsnow(mission,skillcheck = "autogyrogun",wait_runwhile=False):
    screen_check(skillcheck)
    print("###### runwhilecampsnow process ######")
    time.sleep(1)
    click("s",distance=1.5)
    click("q",distance=1.3)
    time.sleep(1)
    for i in range(790,1100,50):
        pg.click(i,330)
    gotomission(mission,wait_gomission=wait_runwhile)

def runwhileguild(mission,skillcheck = "autogyrogun"):
    screen_check("Firsttailguild")
    screen_check(skillcheck)
    print("###### runwhileguild process ######")
    click("s",distance=1.5)
    click("q",distance=1)
    time.sleep(1)
    pg.click(774,341)
    gotomission(mission)

#---------------------------------904-------------------------------------------------
def run905mol():
    screen_check("autogyrogun")
    print("###### run905mol process ######")
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
    time.sleep(2.5)
    click("3")

def run904():
    screen_check("autogyrogun")
    print("###### run904 process ######")
    click("c",distance=2.3)
    time.sleep(1)
    click("w",distance=10)
    click("s")
    useskill("autogyrogun","1")
    click("w",distance=1.5)

def run604():
    screen_check("autogyrogun")
    print("###### run604 process ######")
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

def run602():
    screen_check("autogyrogun")
    click("s")
    useskill("autogyrogun","1")
    useskill("buildbot","9",contime=3)
    #---------------1-----------------
    click("e",distance=2)
    click("w",distance=2)
    click("e",)
    useskill("autogyrogun","1")
    #---------------2-----------------
    click("w",distance=1.5)
    click("e")
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)
    #--------------3th syncolmole-----
    click("q",distance=2)
    useskill("autogyrogun","1")
    #---------------4-------------------
    click("s",distance=2)
    click("q")
    useskill("reload","7",wait=False)
    useskill("autogyrogun","1")
    #---------------5-------------------
    click("s",distance=2)
    click("e",distance=4)
    click("w",distance=2)
    useskill("autogyrogun","1")
    click(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    #---------------6-------------------
    screen_check("keygo")
    click("w",distance=0.5)
    click("e",distance=4.5)
    click("s",distance=5)
    #------------go to final-------------

def run403():
    screen_check("autogyrogun")
    print("###### run403 process ######")
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
def pausewhiledrop(name):
    screen_check("postbutton")
    print(f"###### pausewhiledrop {name} process ######")
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
    print(f"###### takescreenshot {name} process ######")
    screenshotraw_raw = pg.screenshot()
    screenshotraw_raw.save(path + r"raw\\" + name + subfixname +r".PNG")
    screenshot_raw = pg.screenshot(region=(569,24,800,600))
    screenshot_raw.save(path + name + subfixname +r".PNG")
    print("##### take screenshot " + time.ctime() + " #########")

def gocamp():
    screen_check('postbutton')
    screen_check('MissionCamp')
    print("###### gocamp process ######")
    time.sleep(1)
    pg.click(890,484)

#----------------------------------------------------------------------------

def allin604():
    run604()
    collecrewarditemByImg("pumkincoin")
    collecrewarditemByImg("redstone")
    collecrewarditemByImg("pumkincannon")
    pausewhiledrop("pumkincannon")
    takescreenshot("604")
    gocamp()
    runwhilecamp("604")

def allin905smol():
    skipshadowboss()
    run905mol()
    gocamp()
    runwhilecamp("905")

def allin905chm():
    skipshadowboss()
    run905chm()
    collecrewarditemByImg("shadowbow")
    collecrewarditemByImg("shadowpowder")
    gocamp()
    runwhilecampchm("905")

def allin403():
    run403()
    collecrewarditemByImg("hpposion3")
    gocamp()
    runwhilecampsnow("403",wait_runwhile=True)

def allin602():
    run602()
    collecrewarditemByImg("copperore")
    gocamp()
    runwhilecamp("602",wait_runwhile=True)

def allin703():
    screen_check("gilshot")
    click("w",distance=1)
    collecrewarditemByImg("greatstring")
    collecrewarditemByImg("ironstring")
    gocamp()
    runwhilecamprab("703",skillcheck="gilshot",wait_runwhile=True)
#----------------------------------------------------------------------------
# 
keyboard = Controller()
time.sleep(0.5)
while True:
    allin604()