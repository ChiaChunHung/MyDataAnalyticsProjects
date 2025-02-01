"""
File: extension4_MidpointKarel.py
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


# Extension4作法(似MiddlepointKarel.py的做法)：中點公式『(頭的X座標＋尾的X座標)/2』
# 將X軸坐標用Beeper數量來替代，即：1個beeper代表X軸的1單位、6個beepers代表X軸的6單位
# 我把世界拆分成1*1、1*2世界、1*(n>2)的其他世界
def main():
    """
    Karel will use beeper number to represent X-axis coordinates
    and then it will use mid-point formula to find the middle point
    of street one, by adding up the first and last coordinate of its world,
    dividing that number by 2, and then walking forward according to the outcome.
    """
    if not front_is_clear():  # 此處yes區間適用1*1世界
        put_beeper()
    else:  # 此處No區間適用1*2世界、1*(n>2)的其他世界
        move()
        if front_is_clear():  # 此處yes區間適用1*(n>2)的其他世界
            back_to_initial_position()
            find_the_last_coordinate()  # 找出尾座標
            find_the_first_coordinate()  # 找出頭座標
            add_up()  # 做頭座標＋尾座標的動作
            divided_by_2()  # 做除以２的動作並走到中點上
        else:  # 此處no區間適用1*2世界
            put_beeper()


def back_to_initial_position():  # 先回到起始位置，準備開始執行n*n(n>2)世界的找中點行動
    """
    Pre-condition: karel is at (1,2), facing east.
    Post-condition: karel is at (1,1), facing east.
    """
    turn_around()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def find_the_last_coordinate():  # 每往前走一格就把前面一格的beeper全搬過來在加一個beeper，如此就能用beeper數量顯示走了幾步
    """
    Pre-condition: Karel is at (1,1), facing east.
    Post-condition: karel is at (1, last avenue) with beepers below its foot,
    whose number represent the number of avenue oon street 1, and karel faces west.
    """
    put_beeper()
    while front_is_clear():
        while on_beeper():
            pick_beeper()
            move()
            put_beeper()
            turn_around()
            move()
            turn_around()
        move()
        put_beeper()
    turn_around()


def find_the_first_coordinate():  # 即回到(1,1)放一顆beeper做為X軸的1座標
    """
    Pre-condition: Post-condition: karel is at (1, last avenue) with beepers below its foot,
    whose number represent the number of avenue oon street 1, and karel faces west.
    Post-condition: karel is at (1,1) with a beeper under its foot, facing east.
    """
    while front_is_clear():
        move()
    turn_around()
    put_beeper()


def add_up():  # 透過取一放一的方法，把最右邊的beepers數量全部加到最左邊的beepers上
    """
    pre-condition: karel is at (1,1) with a beeper under its foot, facing east.
    post-condition: karel finishes add up all the beepers at (1,1) and (1, last avenue)
    and then place them all at (1,1), facing east.
    """
    move()
    while not on_beeper():
        move()
    turn_around()
    while on_beeper():
        pick_beeper()
        while front_is_clear():
            move()
        turn_around()
        put_beeper()
        while front_is_clear():
            move()
        turn_around()
    while front_is_clear():
        move()
    turn_around()


def divided_by_2():  # 透過取二放一來模仿除以2的動作。取二放一和MidpointKarel.py的作法一樣
    """
    Pre-condition: karel finishes add up all the beepers at (1,1) and (1, last avenue)
    and then place them all at (1,1), facing east.
    Post-condition: karel stands on the middle point of street1 with a beeper below its foot.
    """
    # 把(1,1)當成X軸的座標1；取二放一能夠執行的次數就是中點的單位
    # 舉例：若取二放一能做3次，那就代表中點是3，又(1,1)位置代表X軸上的單位1，故走三格即是中點座標
    while on_beeper():
        pick_beeper()
        if on_beeper():
            pick_beeper()
            move()
        else:
            move()
        if not on_beeper():
            put_beeper()
        else:
            while on_beeper():
                move()
            put_beeper()
        turn_around()
        while front_is_clear():
            move()
        turn_around()
    move()
    while on_beeper():
        pick_beeper()
        move()
    turn_around()
    move()
    move()
    put_beeper()



# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
