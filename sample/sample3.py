#画像を表示するプログラム
from psychopy import visual, core

win = visual.Window()

photo = visual.ImageStim(win, "test.jpeg") # 1. 画像刺激の準備

photo.draw() # 2. 刺激の描画
win.flip()

core.wait(3)

win.close()
