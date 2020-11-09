#key入力までの時間計測
from psychopy import visual, core, event

win = visual.Window()

stopwatch = core.Clock() # stopwatchという名前の時計を用意

for i in range(3):
    step = visual.TextStim(win, i) # 1. 文字刺激の準備
    step.draw()
    win.flip()
    stopwatch.reset()
    resp = event.waitKeys(timeStamped = stopwatch) #key入力の受け取り
    print(resp) #押したkeyと計測時間(s)が配列として取得される

win.close()
