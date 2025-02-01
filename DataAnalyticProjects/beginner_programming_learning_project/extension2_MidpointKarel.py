"""
File: extension2_MidpointKarel.py
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


# Extension2作法(似Extension1)：輪流在street1的頭(最左)和尾(最右)放一顆->直到放到最後一顆，那顆即是中點。
# 放完後beeper在中點上後，再來針對他的左邊和右邊進行清洗，就會出現karel站在中點上且有beeper，而其他地方都沒有beeper。
# 我把世界拆分成1*1、1*2世界、1*(n>2)的其他世界
def main():
    """
    Karel will first discern its world type,and,
    if its world is 1*1, it will leave a beeper and stop; otherwise,
    if its world is n*n (n≥2), it will try to leave a beeper on the corner
    closest to the center of 1st Street, by placing all avenues on street 1
    with beepers and then removing the first and last elements
    continuously until only one remains. The one that remain is
    the one that is at the middle point of street 1.
    """
    if not front_is_clear():                            # 1*1世界適用此問題的yes區間
        put_beeper()
    else:                                               # 1*2世界、1*多世界適用此問題的No區間
        put_till_last_position()
        clean_up()


def put_till_last_position():
    """
    Pre-condition: karel stands at (1,1), facing East.
    Post-condition: if the word is 1*(n≥2), Karel will fill
    up every avenues on street 1 with beepers and then stand
    on the middle point; otherwise, if the world is 1*2,
    karel will stands at (1,1) with a beeper, facing West.
    """
    put_beeper()
    move()
    if front_is_clear():                                # 此處的yes區間適用1*(n>2)世界
        while front_is_clear():
            move()
        put_beeper()                                    # 最左的頭和最右的尾都完成放置Beepers
        turn_around()
        move()                                          # 站到沒有beeper的空格上
        while not on_beeper():                          # 此回圈幫助完成"頭尾一直輪替放beeper直到收斂到中間的空格"
            move()
            if on_beeper():
                turn_around()
                move()
                put_beeper()
                move()
            else:
                pass
        turn_around()
        move()
    else:                                               # No區間則適用1*2世界
        turn_around()
        move()


def clean_up():
    """
    Pre-condition: for 1*(n>2) world, karel stands on the middle point with a beeper.
    Post-condition: for for 1*(n>2) world, karel clean up all beepers on street one, except the one
    at the middle point, and then it will return to the beeper at the middle point.
    """
    if front_is_clear():                                # 此處的yes區間適用1*(n>2)世界
        for i in range(2):                              # 做兩次清洗是因為要請裡中點的左邊和右邊
            move()
            while front_is_clear():
                pick_beeper()
                move()
            pick_beeper()
            turn_around()
            while not on_beeper():
                move()
    else:                                               # No區間適用1*2世界。1*2世界不用進行清洗
        pass


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
