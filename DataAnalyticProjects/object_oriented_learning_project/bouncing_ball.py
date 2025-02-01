"""
File: bouncing_ball.py
Name: Tony
-------------------------
This program simulates the motion trajectory of
a ball dropping from a height and bouncing until it
exits the window, simulation that can only be operated
for three times and will not be interrupted during each
operation.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(20, 20)                                  # 因為從頭到尾球就只有一顆，所以放在全域中當全域變數
switch = True                                         # 開關：控制何時滑鼠點按可讓球下落的動畫重新開始(可避免球下落到一半因滑鼠被點擊而被重新執行)
how_many_lives = 3                                    # 玩家可玩的次數(即：球下落的動畫可被執行的次數)


def main():
    """
    This program simulates a bouncing ball at
    (START_X, START_Y) that has VX as x velocity
    and 0 as y velocity. Each bounce reduces y
    velocity to REDUCE of itself.
    """
    ball.filled = True                                # 因為最開始，當玩家尚未點擊時，就已有一顆球在初始位置，故要在
    window.add(ball, x=START_X, y=START_Y)            # 啟動滑鼠監聽之前，就把球貼到初始位置上。
    onmouseclicked(dropping_process)                  # 接者啟動滑鼠監聽器來等待使用者點擊滑鼠，一但滑鼠被點擊，就讓該顆球執行下落動畫


def dropping_process(_):                              # 因滑鼠資訊根本用不到，故用底線替代(jerry上課教"這種寫法可讓讀者知道此變數未被使用")
    """
    This function triages the conditions
    set off by the clicks of the mouse.
    """
    global switch                                     # 因為全域中的此開關需要一直被Reassign，所以要用global去告知電腦這是全域變數
    global how_many_lives                             # 因為全域中的剩餘可玩次數關需要一直被Reassign，所以要用global去告知電腦這是全域變數
    if switch:                                        # 當開關是開的，就可以進入此區間去執行球下落的動畫
        switch = False                                # 球一開始下落就要關閉此開關，這樣才能防止球下落到一半又因滑鼠點擊而改變原本的重力加速度
        if how_many_lives > 0:                        # 判斷可玩次數是否還有剩，若還有
            drop_till_end()                           # 那就執行drop_till_end()此一下落動畫，
            how_many_lives -= 1                       # 並減少一次剩餘可玩次數
            switch = True                             # 結束該次下落動畫後，要打開開關，讓下一次滑鼠點擊時，球的下落動畫可再次被執行
        else:                                         # 我知道else:pass在style上省略比較好，但寫出來我複習時才會記得這個區間在幹麻，所以先不省。
            pass                                      # 進入此區間，代表已經沒有可玩次數，開關在最後一次的動畫中被關閉後，就沒再被打開過，
    else:                                             # 故使用者之後不管在點擊多少次都是進入此else區間，
        pass
        # 此區間讓動畫在進行時，不會因為使用者重新點擊滑鼠，而被重新執行。
        # 且此區間還可在當剩餘可玩次數歸零時，不會因為使用者再次點擊滑鼠，而讓動畫又可以被執行。


def drop_till_end():
    """
    This function simulates the motion trajectory of
    a ball dropping from a height and bouncing until it
    exits the window.
    """
    ball_v = 0                                        # 先做出一個裝球體下落速度的箱子
    while True:                                       # 讓球體一直做往右下掉並在觸底時向右上反彈，直到球體離開視窗
        ball.move(VX, ball_v+GRAVITY)                 # 球體先往右下掉
        ball_v = ball_v+GRAVITY                       # 球體在下落過程中會因重力而速度遞增
        pause(DELAY)
        if ball.y >= 500:                             # 進入此區間，代表球體觸地，準備讓它回彈
            ball.move(0, -(ball.y-500))               # 確保球體不會在地面以下的空間回彈，而是以地面為基底回彈。因當它跑到地底，就會被這行code直接搬到地面上
            bounce_back_v = -ball_v*REDUCE            # 回彈的速度是碰撞前一刻的速度的九成且是反方向
            while True:                               # 此回圈讓球體一直往上彈直到球體因重力而失去所有速度
                ball.move(VX, bounce_back_v)
                bounce_back_v += GRAVITY              # 球體每往上走一次，速度就會因為重力而減少一次
                pause(DELAY)
                if bounce_back_v >= 0:                # 代表球體已經失去所有速度（不能用==0，因為可能不會有剛好等於零的狀況）
                    break                             # 離開此回圈準備做下一輪的掉落
            ball_v = 0                                # 下一輪掉落開始前，要先把掉落的初始速度歸零，否則會造成下輪掉落的初速是上輪掉落的尾速
        if ball.x >= 800:                             # 此時球體離開視窗，就結束此次下落動畫
            break
    window.add(ball, x=START_X, y=START_Y)            # 下落動畫結束後，直接把球貼回起始位置
    # 從頭到尾只會有一顆球，這行code不是再貼一顆新的球在視窗起始位置，而是把原來已經離開視窗的那顆球貼回去起始位置)










if __name__ == "__main__":
    main()
