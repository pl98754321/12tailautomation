from automatio_main import *

def run905mol():
    screen_check("autogyrogun")
    print("###### run905mol process ######")
    useskill("autogyrogun","1")
    #----------
    press("e",distance=2)
    useskill("buildbot","9",contime=3.5)
    useskill("Reload","7",wait=False)
    useskill("autogyrogun","1")
    useskill("Syncomole","6",wait=False)
    #----------
    press("w",distance=2)
    useskill("autogyrogun","1")
    #----------
    press("q",distance=2)

def run905chm():
    screen_check("bloodbrun")
    press("z",distance=0.3)
    press("s",distance=4)
    press("1")
    time.sleep(0.75)
    press("2")
    time.sleep(2.5)
    press("3")

#-----------------------------------------------------
def allin905mol():
    skip()
    run905mol()
    gocamp()
    runwhilecamp("905")

def allin905chm():
    skip()
    run905chm()
    collecrewarditemByImg("shadowbow")
    collecrewarditemByImg("shadowpowder")
    gocamp()
    runwhilecampchm("905")

#-----------------------------------------------------

while True:
    allin905mol()