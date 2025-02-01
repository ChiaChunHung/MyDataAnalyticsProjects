"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    karel will first identify whether its left has wall
    and then decide what type of action he should take
    in order to draw the checkerboard, using beepers.
    """
    if left_is_clear():
        method_1()
        while left_is_clear():
            move_to_next_line()
            method_2()
            if left_is_clear():
                move_to_next_line()
                method_1()
    else:
        method_1()


def method_1():
    """
    Pre-condition: Karel will stand at far-left avenue, while facing east.
    Post-condition: Karel will fill the odd avenue with beepers,
    and it will return to far-left avenue, facing east.
    """
    put_beeper()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            move()
            put_beeper()
    back_to_start_point()


def back_to_start_point():
    """
    Pre-condition: karel will stand at the far-right avenue, facing east.
    Post-condition: Karel will stand at far-left avenue, facing east.
    """
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    while not facing_east():
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def move_to_next_line():
    """
    Pre-condition: karel is at the far-left avenue on certain street, facing east.
    Post-condition: karel is at the same avenue but on one street above, facing east.
    """
    turn_left()
    move()
    turn_right()


def method_2():
    """
    Pre-condition: Karel will stand at far-left avenue, while facing east.
    Post-condition: Karel will fill the even avenue with beepers,
    and it will return to far-left avenue, facing east.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    back_to_start_point()


# Below is the Second Answer Version of this Question #
# def method_1():
#     put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()
#     turn_left()
#     turn_left()
#     while front_is_clear():
#         move()
#     while not facing_north():
#         turn_left()
#     move()
#     while not facing_east():
#         turn_left()
#
#
# def method_2():
#     if front_is_clear():
#         move()
#         put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()
#     while not facing_west():
#         turn_left()
#     while front_is_clear():
#         move()
#     while not facing_north():
#         turn_left()
#     move()
#     while not facing_east():
#         turn_left()
#
#
# def wrap_up():
#     turn_right()
#     move()
#     while not facing_north():
#         turn_left()
#     if on_beeper():
#         move()
#         turn_right()
#         if front_is_clear():
#             move()
#             put_beeper()
#         while front_is_clear():
#             move()
#             if front_is_clear():
#                 move()
#                 put_beeper()
#     else:
#         move()
#         turn_right()
#         put_beeper()
#         while front_is_clear():
#             move()
#             if front_is_clear():
#                 move()
#                 put_beeper()
#
#
# def turn_right():
#     for i in range(3):
#         turn_left()
#
#
# def main():
#     if left_is_clear():
#         while left_is_clear():
#             method_1()
#             if left_is_clear():
#                 method_2()
#             else:
#                 pass
#         wrap_up()
#     else:
#         put_beeper()
#         while front_is_clear():
#             move()
#             if front_is_clear():
#                 move()
#                 put_beeper()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
