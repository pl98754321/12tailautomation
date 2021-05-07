from automatio_main import *
def run403():
    screen_check("autogyrogun")
    print("###### run403 process ######")
    press("w")
    useskill("autogyrogun","1")
    useskill("buildbot","9",contime=3.5)
    #----------
    press("s",distance=3.5)
    press("q",distance=3)
    useskill("autogyrogun","1")
    #----------
    press("e",distance=3)
    press("s",distance=2)
    press("e",distance=3)
    useskill("autogyrogun","1")
    press(Key.shift)
    useskill("subrab","0",wait=False)
    useskill("syncomole","6",wait=False)
    #----------
    press("q",distance=1.5)
    press("s")
    useskill("autogyrogun","1")
    #----------
    press("q",distance=1.5)
    useskill("reload","7",wait=False)
    useskill("autogyrogun","1")
    useskill("syncomole","6",wait=False)

def allin403(wait = True):
    run403()
    collecrewarditemByImg("hpposion3")
    gocamp()
    runwhilecampsnow("403",wait_runwhile=wait)

while True:
    allin403()