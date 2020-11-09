#windowを開くだけのプログラム

from psychopy import visual, core

win = visual.Window() # 2. 画面を表示する
core.wait(3) # 3. 3秒待つ

win.close()
