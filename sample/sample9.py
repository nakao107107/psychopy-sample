#刺激のランダマイズ
from psychopy import visual, core
import random

win = visual.Window()
stimArray = ["a", "b", "c"]
random.shuffle(stimArray) #刺激をシャッフル

for i in range(3):
    stim = visual.TextStim(win, stimArray[i])
    stim.draw()
    win.flip()
    core.wait(1)

win.close()
