# User
"""
This is an object-oriented program
that creates the animation of a brick breaker game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    # create objects
    graphics = BreakoutGraphics()
    number_of_attempts = 0
    num_of_bricks = graphics.get_brick_num()
    number_of_brick_remove = 0
    # the animation loop
    while True:  # 這個回圈在等待使用者
        if graphics.switch:
            # 代表使用者點按，開關打開並且獲得非零的速度vx＆vy，之後就算使用者再度點按，開關都是開的
            # 且因第二次含以後的點按就算改變get_vx和get_vy的值，user端這裡下方兩行code都不會再被執行到，所以回圈中的球速仍會按照初次點按的速度去跑
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            while True:  # 球的動畫
                # update
                graphics.ball.move(vx, vy)
                # check1：球的四個角是否有人遇到磚塊或板：有遇到則方向(vy)改變，沒遇到則方向(vy)不變
                obj_checker = False
                while True:
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                                               graphics.ball.y)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x,
                                                               graphics.ball.y + graphics.ball_radius * 2)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    may_be_obj = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                                               graphics.ball.y + graphics.ball_radius * 2)
                    if may_be_obj is not None:
                        obj_checker = True
                        break
                    if not obj_checker:
                        break
                if obj_checker:  # 代表四角有一角碰到物件
                    if may_be_obj.y == graphics.paddle.y:
                        graphics.window.add(graphics.ball, x=graphics.ball.x, y=graphics.paddle.y-graphics.ball.height)
                        vy = -vy
                    else:
                        graphics.window.remove(may_be_obj)
                        number_of_brick_remove += 1
                        vy = -vy
                # check2：是否觸及邊界-分成：觸碰兩邊界但沒觸碰上下界，故vy不變vx變；觸碰上下界但沒觸碰左右界，故vx不變vy變
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy
                if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width)/2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    break
                if number_of_brick_remove == num_of_bricks:
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    break
                # pause
                pause(FRAME_RATE)
        else:
            graphics.ball.move(0, 0)            # 當進入此圈，代表使用者未點按，故開關沒打開，vx和vy都是0，所以球看起來就像靜止的
        pause(FRAME_RATE)                       # 每圈都pause，才不會讓螢幕更新速度跟不上電腦運算速度而當機！！
        if number_of_attempts == NUM_LIVES:     # 三命用完，離開遊戲動畫回圈
            break
        if number_of_brick_remove == num_of_bricks:
            break















if __name__ == '__main__':
    main()
