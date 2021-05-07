from automatio_main import *

def run602():
    screen_check("autogyrogun")
    press("s")
    useskill("autogyrogun","1")
    useskill("buildbot","9",contime=3)
    #---------------1-----------------
    press("e",distance=2)
    press("w",distance=2)
    press("e")
    useskill("autogyrogun","1")
    #---------------2-----------------
    press("w",distance=1.5)
    press("e")
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)
    #--------------3th syncolmole-----
    press("q",distance=2)
    useskill("autogyrogun","1")
    #---------------4-------------------
    press("s",distance=2)
    press("q")
    useskill("reload","7",wait=False)
    useskill("autogyrogun","1")
    #---------------5-------------------
    press("s",distance=2)
    press("e",distance=4)
    press("w",distance=2)
    useskill("autogyrogun","1")
    press(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    #---------------6-------------------
    skip("bodas")
    time.sleep(2.5)
    press("w",distance=0.5)
    press("e",distance=4.5)
    press("s",distance=1)
    time.sleep(17.5)
    press("s",distance=5)
    #------------go to final-------------

def allin602():
    run602()
    collecrewarditemByImg("copperore")
    collecrewarditemByImg("ironpowder")
    gocamp()
    runwhilecamp("602")