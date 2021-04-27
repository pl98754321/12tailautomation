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
def runwhilmapmine(map):
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

keyboard = Controller()
pg.mouseDown(button='right')
time.sleep(1)
pg.drag(30, 0, 2, button='right')
time.sleep(1)
pg.mouseUp(button="right")
#