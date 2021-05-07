from automatio_main import *

def run604():
    screen_check("autogyrogun")
    print("###### run604 process ######")
    useskill("autogyrogun","1")
    #----------
    press("q",distance=1.7)
    press("w",distance=0.85)
    useskill("buildbot","9",contime=4)
    useskill("autogyrogun","1")
    #----------
    press("e",distance=3.4)
    useskill("autogyrogun","1")
    press(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    useskill("reload","7",wait=False)
    #----------
    press("w",distance=2)
    useskill("autogyrogun","1")
    #----------
    press("q",distance=3)
    press("w")
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)
    press("q",distance=1)

def allin604():
    run604()
    collecrewarditemByImg("pumkincoin")
    collecrewarditemByImg("redstone")
    collecrewarditemByImg("pumkincannon")
    pausewhiledrop("pumkincannon")
    takescreenshot("604")
    gocamp()
    runwhilecamp("604")

while True:
    allin604()