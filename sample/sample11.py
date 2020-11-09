#windowに動画を表示するプログラム

from psychopy import visual, core # 必要なツールの指定

win = visual.Window() # 画面を表示する

movie = visual.MovieStim3(win, 'test.mp4')
print(movie.duration)

movie.play()

#動画の再生（フレームごとにdrawを読み込まなくてはいけないらしい　面倒くさい）
while True
    movie.draw()
    win.flip()
