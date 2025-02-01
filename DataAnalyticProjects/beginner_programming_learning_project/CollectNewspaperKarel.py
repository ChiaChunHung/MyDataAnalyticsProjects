"""
File: CollectNewspaperKarel.py
Name: Tony
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    karel will go to pick the newspaper
    and then bring it back to its initial position.
    """
    walk_to_the_newspaper()
    bring_it_back()


def walk_to_the_newspaper():
    """
    pre-condition: karel is at its initial position (4,3), facing East
    post-condition: karel is on beeper at (3,6), facing East
    """
    turn_right()
    move()
    turn_left()
    while not on_beeper():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def bring_it_back():
    """
    pre-condition: Karel is on beeper at (3,6), facing East.
    post-condition: Karel is at is initial position (4,3), facing East
    """
    pick_beeper()
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


# Below is the Second Answer Version of this Question #
# def main():
#     """
#     karel will go to pick up the newspaper,
#     return to its original position, and then put down the newspaper.
#     """
#     walk_to_the_newspaper()
#     bring_it_back()
#
#
# def walk_to_the_newspaper():
#     """
#     pre-condition: karel is at (4,3)
#     post-condition: karel will step on the news paper at (3,6)
#     """
#     while front_is_clear():
#         move()
#     turn_right()
#     move()
#     turn_left()
#     move()
#
#
# def turn_right():
#     for i in range(3):
#         turn_left()
#
#
# def bring_it_back():
#     """
#     pre-condition: karel steps on the news paper at (3,6)
#     post-condition: karel is at its original position at (4,3)
#     """
#     pick_beeper()
#     while not facing_west():
#         turn_left()
#     while front_is_clear():
#         move()
#     turn_right()
#     move()
#     put_beeper()
#     turn_right()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
