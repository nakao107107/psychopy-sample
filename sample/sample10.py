#key入力, 入力までの時間をファイル出力する
from psychopy import visual, core, event
import pathlib

current_folder = pathlib.Path(__file__).parent
new_filename = "first_datafile.csv"
new_filepath = current_folder/new_filename

datafile = open(new_filepath, mode = 'a')

win = visual.Window()

stopwatch = core.Clock() # stopwatchという名前の時計を用意

for i in range(3):
    step = visual.TextStim(win, i) # 1. 文字刺激の準備
    step.draw()
    win.flip()
    stopwatch.reset()
    resp = event.waitKeys(timeStamped = stopwatch) #key入力の受け取り
    datafile.write(resp[0][0]+','+str(resp[0][1])+'\n')

win.close()
datafile.close()
