import pyautogui as pg
import time

def Tellstock(word,numcheck):
    if pg.locateOnScreen(path + word + r".PNG", confidence=0.9) != None: 
        pg.write("\\ " + word + " \\")
        time.sleep(0.5)
        print('- ' + word + ' -')
        numcheck += 1
        return numcheck

path = r"C:\Users\plem67\Desktop\New folder (2)\ScreenCheck\\"
while True:
    if pg.locateOnScreen(path+r"\name.PNG", confidence=0.9) == None: 
        print("DontHaveMarkey")
        break
    i= 0 
    stocklist = ["GiantDrug","knots","StrawberrySunday","SmallJunk"]
    print("working" + time.ctime())
    pg.press('enter')
    time.sleep(1)

    for item in stocklist:
        i = Tellstock(item,i)

    pg.press('enter')
    print(i)
    if i == 0 :
        print("break")
        break

    time.sleep(20)