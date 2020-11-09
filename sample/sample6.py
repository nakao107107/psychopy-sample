#刺激位置をずらす

from psychopy import visual, core # 必要なツールの指定

win = visual.Window() # 画面を表示する

hello = visual.TextStim(win, "hello world") # 1. 文字刺激の準備
hello.setPos([0, 0.5])

hello.draw() # 2. 刺激の描画
win.flip() # 3. 画面に反映

core.wait(3) # 3秒待つ

win.close() # 画面を閉じる
