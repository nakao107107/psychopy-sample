#key入力の受け取り
from psychopy import visual, core, event

win = visual.Window()

for i in range(3):
    step = visual.TextStim(win, i) # 1. 文字刺激の準備
    step.draw()
    win.flip()
    resp = event.waitKeys() #key入力の受け取り
    #event.waitKeys(keyList = ['a', 'b']) # keyの指定も可能
    print(resp) #押されたkeyは返り値として取得できる

win.close()
