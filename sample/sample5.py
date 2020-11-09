#刺激の系列表示（テキストと画像を交互に３回表示する）
from psychopy import visual, core

win = visual.Window()

hello = visual.TextStim(win, "hello world!") # 1. 文字刺激の準備
photo = visual.ImageStim(win, "test.jpeg") # 1. 画像刺激の準備

for i in range(3):
    hello.draw()
    win.flip()
    core.wait(3)

    photo.draw() # 2. 刺激の描画(コードの順序がレイヤー順になる)
    win.flip()
    core.wait(3)


win.close()
