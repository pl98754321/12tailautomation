
from pynput.keyboard import Key, Controller
import pyautogui as pg
import time

def filelocate(name):
    path = r"C:\Users\plem67\Desktop\New folder (2)\automation\\"
    return path + name + r".png"

def screen_check(name,percent = 0.9):
    while True:
        if pg.locateOnScreen(filelocate(name), confidence=percent) != None:
            print("---- " + name + " complete----")
            break

def collecrewarditemByImg(name):
    screen_check("postbutton")
    while pg.locateOnScreen(filelocate(name),confidence=0.7,region=(725,330,225,100)) != None:
        x,y = pg.locateCenterOnScreen(filelocate(name),confidence=0.7,region=(725,330,225,100))
        pg.click(x, y)
        time.sleep(0.9)

collecrewarditemByImg() #<-------- ใส่ชื่อไฟล์ในนี้
