"""
File: extension1_MidpointKarel.py
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


# Extension1作法：先把Street1全撲滿beepers->接者開始一直做頭撿一個，尾撿一個->直到撿到最後一個，該beeper的位置就是中點
# 我把世界拆分成1*1、1*2世界、1*(n>2)的其他世界
def main():
    """
    Karel will first discern its world type,and, if its world is 1*1,
    it will leave a beeper and stop; otherwise, if its world is n*n (n≥2),
    it will try to leave a beeper on the corner closest to the center of 1st Street,
    by placing all avenues on street 1 with beepers and then removing the first and last elements
    continuously until only one remains. The one that remain is
    the one that is at the middle point of street 1.
    """
    if not front_is_clear():  # 1*1世界適用此問題的yes區間
        fill_one_line()
    else:  # 1*2世界、1*多世界適用此問題的No區間
        fill_one_line()
        back_to_initial_position()
        pick_till_the_last()


def fill_one_line():
    """
    Pre-condition: karel stands at (1,1), facing East.
    Post-condition: Karel fill up every avenues on street 1 with beepers,
    then standing at (street1, last avenue) and facing East.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    # Karel is at (street1, last avenue), facing east


def back_to_initial_position():  # 回到起始位置，準備開始執行1*n(n>2)世界的找中點行動
    """
    Pre-condition: Karel fill up every avenues on street 1 with beepers, facing East.
    Post-condition: karel stands at (1,1), facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    # Turning left two-times means turning around
    turn_left()
    turn_left()


def pick_till_the_last():
    """
    Pre-condition: Karel fill up every avenues on street 1 with beepers, facing East.
    Post-condition: karel find the middle point of street 1.
    """
    pick_beeper()
    move()
    # 取完最左邊第一個Beeper
    if front_is_clear():  # 此問題的yes區間可以幫助1*(n≥2)的世界找到中點
        while front_is_clear():
            move()
        pick_beeper()
        turn_around()
        move()
        # 取完最右邊的beeper
        # 兩邊的Beeper都取完，並走到剩餘中間的beeper上
        while on_beeper():  # 邊移動邊幫我找左和右的邊緣並且幫我把邊緣慢慢往中點收斂
            move()
            if not on_beeper():
                turn_around()
                move()
                pick_beeper()
                move()
            else:
                pass
        # 收斂到中點的左或右邊
        turn_around()  # 接者回到中點放一顆
        move()
        put_beeper()
    else:  # No區間，代表是1*2世界。故此時停下來就剛好站在1*2世界的中點上且有beeper在腳下
        pass




# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
