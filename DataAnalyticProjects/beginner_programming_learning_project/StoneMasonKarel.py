"""
File: StoneMasonKarel.py
Name: Tony
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will first fill evey pillars of evey arches with beepers except the last arch.
    Once these tasks are completed, Karel will proceed with final wrap up.
    """
    turn_left()
    while right_is_clear():
        fill_up()
        move_to_next_pillar()
    wrap_up()


def fill_up():
    """
    Pre-condition: Karel is at the bottom of the pillar, facing North.
    Post-condition: Karel is at the top of the pillar, facing North.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def move_to_next_pillar():
    """
    Pre-condition: Karel is at the top of the pillar, facing North.
    Post-condition: Karel is at the bottom of the pillar, facing North.
    """
    while not facing_south():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    for i in range(4):
        move()
    turn_left()


def wrap_up():  # karel will fill up the last pillar and finish the job.
    """
    Pre-condition: Karel is at the bottom of the last pillar, facing North.
    Post-condition: Karel is at the at the bottom of the last pillar, facing East.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()
    while not facing_south():
        turn_left()
    while front_is_clear():
        move()
    turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
