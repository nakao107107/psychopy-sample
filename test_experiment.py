#テスト用の心理物理学実験プログラム
from psychopy import visual, core, event # 必要なツールの指定
import pathlib
import random
import datetime

data_folder = pathlib.Path('./data')
now = datetime.datetime.now()
random.seed(now.microsecond)
#現在時刻からユニークなファイル名を作成
filename = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".csv"
filepath = data_folder/filename

datafile = open(filepath, mode = 'a')
win = visual.Window(color=(-1.0, -1.0, -1.0),opacity=1.0,fullscr=True) # 画面を表示する

fixationPoint = visual.TextStim(win, "+")
stim = visual.MovieStim3(win, 'test.mp4')

stim.play()

stopwatch = core.Clock()
stimVideoNumArray = ["1","2"]

for i in range(3):
    #注視点表示
    random.shuffle(stimVideoNumArray)
    stimVideoNum = stimVideoNumArray[0]
    stim = visual.MovieStim3(win, 'rc/' + stimVideoNum + '.mp4')
    fixationPoint.draw()
    win.flip()
    core.wait(1)
    #動画再生
    while True:
        stim.draw()
        win.flip()
        resp = event.getKeys(timeStamped = stopwatch)
        if resp:
            datafile.write(stimVideoNum + ',' + resp[0][0]+','+str(resp[0][1])+'\n')
            stopwatch.reset()
            break

win.close() # 画面を閉じる
