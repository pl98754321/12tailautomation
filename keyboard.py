from pynput.keyboard import Key, Controller
import pyautogui as pg
import time
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
        path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
        if pg.locateOnScreen(path + name + r".PNG", confidence=percent) != None:
            print("---- " + name + " complete----")
            break

#-----------------------------------------------------------------------

def skipshadowboss():
    screen_check("shadowgod")
    path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
    while pg.locateOnScreen(path + r"shadowgod.PNG", confidence=0.9) != None:
        pg.click(847,321)


def run905():
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
    

def gocamp():
    screen_check('postbutton')
    screen_check('MissionCamp')
    pg.click(890,484)

def runwhilemine(mission):
    screen_check("autogyrogun")
    click("q",distance=2)
    click("w",distance=0.5)
    for i in [800,880,950,1000]:
        pg.click(i,330)
    screen_check(mission)
    if mission == "905800600":
        screen_check("createdes800600")
        pg.click(1281,412) #ปุ่มสร้างแตกต่าง
    else:
        screen_check("create800600")
        pg.click(1216,415) #click create
    screen_check("start800600")
    pg.click(1216,415) #click start

#---------------------------------------------

def runwhiledes(mission):
    screen_check("FirsttailDes")
    screen_check("Fatalstike")
    click("q",distance=3)
    click("w",distance=1)
    for i in [1064,1000]:
        pg.click(i,382)
    screen_check(mission)
    screen_check("create800600")
    pg.click(1212,411) #click create

def run703():
    screen_check("Fatalstike")
    pg.hotkey("alt","x")

def checkready():
    path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
    while pg.locateOnScreen(path + r"kkk.PNG", confidence=0.6) == None: #คนพิมพ์ kkk
        print("donthave")
    time.sleep(1)
    pg.click(1212,7411) #click create

#----------------------------------------------------------------------------------

def run904():
    screen_check("autogyrogun")
    click("c",distance=2.3)
    time.sleep(1)
    click("w",distance=10)
    click("s")
    useskill("autogyrogun","1")
    click("w",distance=1.5)

keyboard = Controller()
while True:
    skipshadowboss()
    run905()
    #runwhilemine("905800600")

