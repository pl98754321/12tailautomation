from automatio_main import *

def allin703():
    screen_check("gilshot")
    press("w",distance=1)
    collecrewarditemByImg("greatstring")
    collecrewarditemByImg("ironstring")
    gocamp()
    runwhilecamprab("703",skillcheck="gilshot",wait_runwhile=True)

while True:
    allin703()