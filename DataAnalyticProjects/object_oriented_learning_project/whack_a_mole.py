"""
File: whack_a_mole.py
Name: Chia-Chun Hung
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700  # Jerry試過的還不錯的pause毫秒數

# Global variables (都放變數就好，若要做其他操作，不要在此區做)
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='Whack a Mole')
score = 0  # 製作裝積分用的變數箱子
score_label = GLabel('Score=>' + str(score))  # 製造幾分版：(字串＋數字轉字串)再由GLabel變成文字物件


def main():
    onmouseclicked(remove)  # 放在回圈外即可，因為此mouse drive的絕招，開了就不會停，所以本來就是一直開的回圈
    score_label.font = '-80'
    window.add(score_label, x=0, y=score_label.height)  # 把文字物件貼在window上
    # 用回圈來讓他自動在不同位置開圖
    while True:  # 小心這個回圈是無限回圈，換言之該回圈無法離開，故他的下方離開此回圈的區間的內容不會被執行到
        # 每一圈都會因為該行code『img = GImage('mole.png')』被執行而去從路徑位置上開一張新的地鼠的圖，並存到img中，此時img是一個物件
        # 新的物件有了後，就把它貼在畫布上，故只有最後一張圖會叫img，其他都會被覆蓋掉。
        img = GImage('mole.png')
        # 每一圈都生成一個隨機但不超出window的xy座標
        random_x = random.randint(0, window.width-img.width)
        random_y = random.randint(0, window.height-img.height)
        # 每一圈都把新生出的物件(新開出的那張圖)貼上新的隨機座標
        window.add(img, x=random_x, y=random_y)
        # 每圈都要pause幾豪秒，因為電腦運算太快，不pause()，會導致圖爆
        pause(DELAY)


def remove(mouse):  # mouse是自訂的變數箱名稱
    global score
    # 因為全域中的score是整數，所以電腦一開始會把全域中的score當作是常數，但常數無法在Function中被更動(Reassign)，
    # 所以你在函數中對score+=1，電腦會告知他不理解你該行code。這時的解決方法就是：你在function中加入global score指令，
    # 這樣即可告訴電腦，在全域中的score並不是常數，而是全局變量，所以可以被更動(Reassign)，這樣你就可以對全域中的score去做Reassign。

    maybe_object = window.get_object_at(mouse.x, mouse.y)
    # 獲得滑鼠指標位置的物件

    if maybe_object is not None and maybe_object is not score_label:
        # 當是物件且不是label物件，那就移除掉
        window.remove(maybe_object)
        score += 1
        # score因是全域中的整數，故一開始會被電腦判定為全域中的常數，但常數不可更動且他也不是我們定義的常數，
        # 故應該在上方加入global去告知電腦他不是常數，而是全域變數。
        score_label.text = 'Score=>' + str(score)
        # score_label是全域中的變數，故可以直接更動不用告知電腦
    else:                                                             # 否則(即要嘛是非物件的None，要嘛是label物件)，就不要執行任何操作
        pass







if __name__ == '__main__':
    main()
