"""
File: MidpointKarel.py
Name: 
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


# 作法：取一顆放一顆->全搬過來後在加上一顆->最後的個數告知總共走了幾步->往回做取兩顆走一步直到中點
# 我把世界拆分成1*1、1*2世界、1*(n>2)的其他世界
def main():
    """
    Karel will first discern its world type,and, if its world is 1*1,
    it will leave a beeper and stop; otherwise, if its world is n*n (n≥2),
    it will try to leave a beeper on the corner closest to the center of 1st Street,
    by using beepers to represent the avenue number of street 1 at the far right avenue
    and then moving one step forward every time it picks up two beeper.
    """
    if not front_is_clear():                 # 1*1世界適用此問題的yes區間（此處是針對1*1世界所設的指令）
        put_beeper()
    else:                                    # 1*2世界、1*多世界適用此問題的No區間（此處即是針對其他世界所設的指令）
        obtain_avenue_number()               # 取得走到底需要多少步數(用beeper數量代替步數)
        find_the_mid_point()                 # 總步數上每兩取顆走走一步，來模仿總步數除2。接者就可以找到中點。


def obtain_avenue_number():                  # 每往前走一格就把前面一格的beeper全搬過來在加一個beeper，如此就能用beeper數量顯示走了幾步
    """
    Pre-condition: karel stands at (1,1), facing East.
    Post-condition: Karel uses beeper number to represent how many step it moves,
    at the far right avenue of street, facing East.
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
        put_beeper()                         # 結束後Karel會站在最後一格告訴你總步數且頭朝向East。


def turn_around():                           # turning left two times means turning around
    turn_left()
    turn_left()


def find_the_mid_point():
    """
    Pre-condition: Karel uses beeper number to represent how many step it moves,
    at the far right avenue of street, facing East.
    Post-condition: kare will stand at the middle point of street one, facing East
    """
    # 每取兩個往前走一格放置路標，若遇到放過的路標就繼續走到沒有放過路標的位置去放置路標
    # 放置完路標後，去把路標全部撿起來，最後一個路標的位置就是中點位置了
    turn_around()
    while on_beeper():                      # 整個迴圈就是一直做“撿兩個走一步並放一beeper作為個路標”的工作
        pick_beeper()
        if on_beeper():                     # 設此條件是因為奇數世界取到最後會有無法一次取兩顆的狀況
            pick_beeper()
            move()
        else:                               # 此處為：奇數世界取到只剩一顆，取完後沒有下一顆可以取的狀況時，karel就只需要往前走即可
            move()
        if not on_beeper():                 # 為每一步走過的路都放上beeper做為路標
            put_beeper()
        else:
            while on_beeper():              # 每走新的一步，都得在上一步的路標位置的下一步放置新路標
                move()
            put_beeper()
        turn_around()                       # 放完路標就轉身準備回去原先的總Beeper數量上，以做下一輪迴圈
        while front_is_clear():
            move()
        turn_around()                       # 此時karel放完該步的標並且回到了street1的最右側，頭朝西
    move()                                  # 站到放過的路標上
    if front_is_clear():
        # 排除1*1世界，唯獨1*2世界會出現往回全部取回路標時，中點左邊的那格是牆壁的狀況，
        # 所以他不像其他世界一樣需要全部取回並走到中點的左邊，在往回一格。
        # 故針對1*2世界，這裏就得要進入else去做pass；而其他世界則是走到中點左邊的一格後，往回走一格回到中點
        # 其他世界則是把所有beepers全部取回，最終會走到中點的左邊，故在往回一格就是中點位置並放置路標即可。
        while on_beeper():
            pick_beeper()
            move()
        turn_around()
        move()
        move()
        put_beeper()
    else:
        pass




# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
