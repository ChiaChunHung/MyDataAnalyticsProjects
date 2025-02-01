"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10                                   # 常數，用來控制火箭大小。會有牽一髮動全身的特性。


def main():
    """
    This program use nested for loop to print
    out a rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():                                 # 此function幫我製造出火箭頭
    """
    This function will print the head
    of the rocket.
    """
    for i in range(SIZE):                   # 最外圈控制列數，SIZE多少就幾列且i==0,1,2...
        for j in range(SIZE-i):             # 內圈控制每一欄
            print(' ', end='')              # 第一列印出三個空格、二列兩個、一列一個。用, end=""代表會連在一起
        for j in range(i+1):
            print('/', end='')              # 第一列印出一個/、二列兩個、三列三個
        for j in range(i+1):
            print('\\', end='')             # 第一列印出一個\、二列兩個、三列三個
        for j in range(SIZE-i):
            print(' ', end='')              # 第一列印出三個空格、二列兩個、三列一個
        print('')                           # 每做完一列要換行，不然會變成平行的印出來


def belt():                                 # 此function幫我製造出聯節
    """
    This function will print the belt
    of the rocket.
    """
    print('+', end='')                      # 最左邊放一個正而已，不用回圈。
    for i in range(2*SIZE):                 # SIZE是1時放兩個、2時放4個，所以=、SIZE的關係是兩倍
        print('=', end='')
    print('+', end='')                      # 這樣代表print完這個+號後不會行，但下一行code又幫我換行
    print('')                               # 所以，48+49行可改成單行的print('+')，意思一樣。因為後面沒有寫end=啥時，代表預設換行


def upper():                                # 此function幫我製造出火箭上半身
    """
    This function will print the upper
    part of the middle of the rocket.
    """
    for i in range(SIZE):                   # SIZE是多少，上半身就幾列
        print('|', end='')                  # 每一列的最左邊的｜，印出來後不可換行
        for j in range(SIZE-1-i):           # 上半身的點點的數量由上到下是SIZE-1-i：第一列有2個、二列有1個、三列有0個...
            print('.', end='')
        for j in range(i+1):                # 第一列時，/\有一組；第二列時，/\有兩組；第三列時/\有三組。
            print('/', end='')              # 一組/\就是print(/)再print(\)
            print('\\', end='')
        for j in range(SIZE-1-i):           # 右半邊的點點和左半邊的規則一樣
            print('.', end='')
        print('|')                          # 每一列的最右邊的｜，印出來後要換行


def lower():
    """
    This function will print the lower
    part of the middle of the rocket.
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')              # “.”一定要先print，這樣進入下一回圈才有可能先出“.”再出\/
        for j in range(SIZE-i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        print('|')










# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
