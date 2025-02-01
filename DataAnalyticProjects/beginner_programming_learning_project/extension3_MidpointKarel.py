"""
File: extension3_MidpointKarel.py
Name: Tony
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


# Extension3作法：對角線找到交點後往下就是中點 !
# 這裏我把世界分成1*1、2*2和其他世界；而其他世界又分成奇數世界和偶數世界
# 奇數世界的交點會被放兩次beeper，故可用“若取了一個beeper後下面還有beeper"來測出交點位置，接者直直往下就是中點位置。
# 偶數世界不會有交點，但中心beeper的左邊會多一顆。
# 故可以在測世界時，使用“每走一步測一次左邊有沒有多一顆”，再疊加“取了一個beeper後，腳下還有沒有多一顆“，
# 來測出奇數和偶數世界的中心位置，接者中心位置往下走就是中點。
def main():
    """
    Karel will first discern its world type,and, if its world is 1*1,
    it will leave a beeper and stop; if its world is 2*2, it will leave a
    beeper on (1,2) and stop; and if its world is n*n (n>2), it will try to
    leave a beeper on the corner closest to the center of 1st Street,
    by finding the intersection point of the diagonals of its square world and
    putting a beeper on street 1, right below that intersection point to
    indicate the middle point of street 1.
    """
    if front_is_clear():  # 此處的yes區間是為了2*2和n*n(n>2)世界
        move()
        if not front_is_clear():  # 此處的yes區間是為了2*2世界
            put_beeper()
        else:  # No區間是為了n*n(n>2)世界
            turn_around()
            move()
            turn_around()
            # 回到起始位置，準備開始執行n*n(n>2)世界的找中點行動
            create_the_dia()  # 造出正方形裡的兩條對角線相交的點
            clean_up_and_indicate_the_mid()  # 接者在把對角線beepers清乾淨的過程中，抓出交點位置，並往下找出Street1中點
            back_to_beeper()  # 全部清完後，站回到位在中點的beeper上
    else:  # 此處的No區間是為了1*1世界
        put_beeper()


def create_the_dia():  # karel會先創造出左下往右上的對角線，再創造出左上往右下的對角線
    """
    Pre-condition: karel is at (1,1), facing east.
    Post-condition: karel finishes placing beepers on the 2 diagonals
    and stands at (1, last avenue), facing west.
    """
    turn_left()
    while right_is_clear():  # 當右手為空，一直幫我在左下往右上的對角線上放置beeper
        put_beeper()
        turn_right()
        move()
        turn_left()
        move()
    put_beeper()  # 解決OBBO問題
    turn_left()
    while front_is_clear():
        move()
    while not facing_south():
        turn_left()
    while left_is_clear():  # 當左手為空，一直幫我在左上往右下的對角線上放置beeper
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
    put_beeper()  # 解決OBBO問題
    turn_right()


def clean_up_and_indicate_the_mid():  # 邊清洗，邊幫我找Street1中點
    """
    Pre-condition:karel finishes placing beepers on the 2 diagonals
    and stands at (1, last avenue), facing west.
    Post-condition: karel will clean up all the beepers on diagonals, indicate the middle
    point on street 1 by placing one beeper at that location, and then stand at top right,
    facing south.
    """
    turn_right()
    while left_is_clear():                            # 由右下往左上清洗
        pick_beeper()
        turn_left()
        move()
        turn_around()
        if on_beeper():                               # 此處yes區間是為了找出偶數世界的中心點(因為偶數的中心處的左邊會多一個beeper)
            turn_right()
            while front_is_clear():                   # 走到偶數世界的這一個中心的正下方，就是street1的中點
                move()
            put_beeper()                              # 放置beeper在street1中點上
            turn_around()
            move()
            while not on_beeper():
                move()
            move()                                    # 站到同條對角線上的下一個beeper繼續做右下往左上的清洗
        else:                                         # 此處No區間是為了找出奇數世界的對角線交點(因為奇數世界的中心會被放兩次beeper)
            move()
            turn_left()                               # 因為左邊沒有多一顆，所以站回到原位置上看有沒有第二顆在腳下
            if on_beeper():                           # 此處yes區間代表剛剛取完一顆後腳下還有剩一顆，所以原本此位置有兩顆，這裏是奇數世界的中心
                put_beeper()                          # 放一顆回去讓該位置仍然保持有兩顆，等等清另一條對角線時，再來抓出這點以找出street1中點
                turn_left()
                move()
                turn_right()
                move()                                # 標示完中心後進到對角線上的下一個beeper繼續做清洗
            else:                                     # 此處No區間是當沒有找到奇數世界或偶數世界的對角線交點時要做的事：到對角線上的下一個beepers
                turn_left()
                move()
                turn_right()
                move()
    pick_beeper()                                     # 處理最左上那一顆beeper
    turn_around()
    while front_is_clear():                           # 回到左下
        move()
    turn_around()
    while right_is_clear():                           # 左下往右上清洗
        pick_beeper()
        if on_beeper():                               # 剛剛第一輪清洗時，有順便標出奇數世界中心位置(即有兩顆beepers的位置)，故此處用此條件抓出之
            turn_around()
            while front_is_clear():                   # 奇數世界中心位置直直往下對到street1上，即是中點
                move()
            put_beeper()
            turn_around()
            move()
            while not on_beeper():                    # 回到正方形中心
                move()
        else:                                         # 還未找到正方形中心前應該做的事：走到對角線上的下一個beeper上
            turn_right()
            move()
            turn_left()
            move()
    pick_beeper()                                     # 把左下到右上回圈中無法清除的最右上那顆清掉
    turn_around()


def back_to_beeper():
    """
    Pre-condition: karel clean up all the beepers on diagonals, indicate the middle
    point on street 1 by placing one beeper at that location, and then stand at top right,
    facing south.
    Post-condition: karel stands at the middle point of street 1, with a beeper below its foot.
    """
    while front_is_clear():
        move()
    turn_right()
    while not on_beeper():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
