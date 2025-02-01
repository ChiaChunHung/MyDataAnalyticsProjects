# User
"""
This is an object-oriented program
that creates the animation of a brick breaker game with
more levels and enhanced content!!
"""


from campy.gui.events.timer import pause
from extensions_breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
trash_switch = True


def main():
    # set start scene obj on window
    graphics = BreakoutGraphics()
    # 放上積分版
    graphics.window.add(graphics.trash_collect, x=graphics.window.width-graphics.trash_collect.width-20,
                        y=graphics.window.height)
    # 放上幾命
    graphics.window.add(graphics.live_label1, x=0, y=graphics.window.height)

    # 開場動畫
    graphics.window.add(graphics.start_scene_bg)
    graphics.window.add(graphics.start_warning, x=(graphics.window.width - graphics.start_warning.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.5-60)
    graphics.window.add(graphics.story_line0, x=(graphics.window.width - graphics.story_line0.width) / 2,
                        y=(graphics.window.height-graphics.earth.height)//1.5-20)
    graphics.window.add(graphics.earth, x=(graphics.window.width-graphics.earth.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.25)
    graphics.window.add(graphics.story_line1, x=(graphics.window.width-graphics.story_line1.width)/2,
                        y=(graphics.window.height-graphics.earth.height)//1.5)
    graphics.window.add(graphics.story_line2, x=(graphics.window.width-graphics.story_line2.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5+20)
    graphics.window.add(graphics.story_line3, x=(graphics.window.width-graphics.story_line3.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5+40)
    graphics.window.add(graphics.story_line4, x=(graphics.window.width - graphics.story_line4.width)/2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 60)
    graphics.window.add(graphics.story_line5, x=(graphics.window.width - graphics.story_line5.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 80)
    graphics.window.add(graphics.story_line6, x=(graphics.window.width - graphics.story_line6.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 100)
    graphics.window.add(graphics.story_line7, x=(graphics.window.width - graphics.story_line7.width) / 2,
                        y=(graphics.window.height - graphics.earth.height) // 1.5 + 120)
    # start scene obj animation
    scene_ani_speed = -1  # !
    global trash_switch
    while not graphics.story_line7.y <= 0:
        graphics.start_warning.move(0, scene_ani_speed)
        graphics.story_line0.move(0, scene_ani_speed)
        graphics.story_line1.move(0, scene_ani_speed)
        graphics.story_line2.move(0, scene_ani_speed)
        graphics.story_line3.move(0, scene_ani_speed)
        graphics.story_line4.move(0, scene_ani_speed)
        graphics.story_line5.move(0, scene_ani_speed)
        graphics.story_line6.move(0, scene_ani_speed)
        graphics.story_line7.move(0, scene_ani_speed)
        pause(5)
    graphics.window.remove(graphics.story_line0)
    graphics.window.remove(graphics.story_line1)
    graphics.window.remove(graphics.story_line2)
    graphics.window.remove(graphics.story_line3)
    graphics.window.remove(graphics.story_line4)
    graphics.window.remove(graphics.story_line5)
    graphics.window.remove(graphics.story_line6)
    graphics.window.remove(graphics.story_line7)
    graphics.window.remove(graphics.earth)
    graphics.window.add(graphics.click_to_start, x=(graphics.window.width-graphics.click_to_start.width)/2,
                        y=(graphics.window.height-graphics.click_to_start.height)/2)
    # setting the breaker of game's while loop
    number_of_attempts = 0
    num_of_bricks = graphics.get_brick_num()
    number_of_brick_remove = 0

    # 控制黑洞出現的開關，因為只會在敲三十塊磚時出現，其他時候不可重覆貼上
    black_hole_add_switch = True

    # 球的下落動畫
    while True:
        if graphics.switch:
            # 先把背景移除
            graphics.window.remove(graphics.start_scene_bg)
            graphics.window.remove(graphics.click_to_start)
            # 代表使用者點按，開關打開並且獲得非零的速度vx＆vy，之後就算使用者再度點按，開關都是開的
            # 且因第二次含以後的點按就算改變get_vx和get_vy的值，user端這裡下方兩行code都不會再被執行到，所以回圈中的球速仍會按照初次點按的速度去跑
            vx = graphics.get_vx()
            vy = graphics.get_vy()

            # lv30 & 50 個字的速度設定，為避免無法反彈，故還要設開關，即ball_speed_switch
            if 30 <= graphics.trash < 50:
                vy = 12
            if 50 <= graphics.trash:
                vy = 15
            ball_speed_switch = True
            ball_speed_switch2 = True

            # lv30以上黑洞伴隨的石頭的速度設定
            black_hole_vx = 1
            black_hole_vy = 1
            rock_vx = 1
            rock_vy = 1
            rock_vx1 = 1
            rock_vy1 = 1
            rock_vx2 = 1
            rock_vy2 = 1
            rock_vx3 = 1
            rock_vy3 = 1
            rock_vx4 = 1
            rock_vy4 = 1

            while True:  # 球的動畫
                # update

                # lv30球加速
                if graphics.trash == 30 and ball_speed_switch:
                    vy = 12
                    ball_speed_switch = False
                # lv50球加速
                if graphics.trash == 50 and ball_speed_switch2:
                    vy = 15
                    ball_speed_switch2 = False
                # 球移動
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
                        # ball避免卡在paddle上
                        vy = -vy
                    # 避開非磚塊者
                    elif may_be_obj.y == graphics.window.height:
                        pass
                    elif may_be_obj == graphics.trash1:
                        pass
                    elif may_be_obj == graphics.trash2:
                        pass
                    elif may_be_obj == graphics.trash3:
                        pass
                    elif may_be_obj == graphics.trash4:
                        pass
                    elif may_be_obj == graphics.trash5:
                        pass
                    elif may_be_obj == graphics.trash6:
                        pass
                    elif may_be_obj == graphics.trash7:
                        pass
                    elif may_be_obj == graphics.trash8:
                        pass
                    elif may_be_obj == graphics.trash9:
                        pass
                    elif may_be_obj == graphics.warning_asteroid_belt:
                        pass
                    elif may_be_obj == graphics.black_hole_1:
                        pass
                    elif may_be_obj == graphics.black_hole_2:
                        pass
                    elif may_be_obj == graphics.black_hole_3:
                        pass
                    elif may_be_obj == graphics.black_hole_warning:
                        pass
                    elif may_be_obj == graphics.black_hole_warning1:
                        pass
                    elif may_be_obj == graphics.live_label1:
                        pass
                    else:
                        graphics.window.remove(may_be_obj)
                        number_of_brick_remove += 1  # 用來確認還有沒有剩餘的磚塊
                        graphics.trash += 2
                        graphics.trash_collect.text = 'Trash You Collect ' + str(graphics.trash)
                        vy = -vy

                # check2：是否觸及邊界-分成：觸碰兩邊界但沒觸碰上下界，故vy不變vx變；觸碰上下界但沒觸碰左右界，故vx不變vy變
                if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy

                # 掉到地下
                if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width)/2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break
                # 敲完磚塊
                if number_of_brick_remove == num_of_bricks:
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    break

                # lv30前，每10級遭遇一次太空垃圾
                if graphics.trash != 0 and graphics.trash % 10 == 0 and graphics.trash < 30:
                    if trash_switch:
                        trash_switch = False
                        for i in range(4):
                            graphics.window.add(graphics.event_scene)
                            pause(50)
                            graphics.window.add(graphics.event_scene2)
                            pause(50)
                            graphics.window.remove(graphics.event_scene2)
                            pause(50)
                            graphics.window.remove(graphics.event_scene)
                            pause(50)
                        # warning
                        graphics.window.add(graphics.warning_asteroid_belt,
                                            x=(graphics.window.width-graphics.warning_asteroid_belt.width)//2,
                                            y=(graphics.window.height-graphics.warning_asteroid_belt.height)//2+100)
                        trash_x = random.randint(15, graphics.window.width-65)
                        graphics.window.add(graphics.trash1, x=trash_x, y=100)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash2, x=trash_x, y=60)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash3, x=trash_x, y=150)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash4, x=trash_x, y=300)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash5, x=trash_x, y=250)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash6, x=trash_x, y=250)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash7, x=trash_x, y=200)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash8, x=trash_x, y=210)
                        trash_x = random.randint(15, graphics.window.width - 50)
                        graphics.window.add(graphics.trash9, x=trash_x, y=150)
                # 最上面的垃圾還未離開視窗之前
                if not graphics.trash2.y >= graphics.window.height:
                    trash_vx = random.randint(-10, 10)
                    trash_vy = 1
                    graphics.trash1.move(trash_vx, trash_vy)
                    graphics.trash2.move(trash_vx, trash_vy)
                    graphics.trash3.move(trash_vx, trash_vy)
                    graphics.trash4.move(trash_vx, trash_vy)
                    graphics.trash5.move(trash_vx, trash_vy)
                    graphics.trash6.move(trash_vx, trash_vy)
                    graphics.trash7.move(trash_vx, trash_vy)
                    graphics.trash8.move(trash_vx, trash_vy)
                    graphics.trash9.move(trash_vx, trash_vy)

                # 最上面的垃圾離開視窗，故可以把垃圾掉落開關打開，讓下一個10級可以出現垃圾下落
                else:
                    trash_switch = True
                    graphics.window.remove(graphics.trash1)
                    graphics.window.remove(graphics.trash2)
                    graphics.window.remove(graphics.trash3)
                    graphics.window.remove(graphics.trash4)
                    graphics.window.remove(graphics.trash5)
                    graphics.window.remove(graphics.trash6)
                    graphics.window.remove(graphics.trash7)
                    graphics.window.remove(graphics.trash8)
                    graphics.window.remove(graphics.trash9)
                    graphics.window.remove(graphics.warning_asteroid_belt)

                # 確認trash2有沒有撞上板
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x, graphics.trash2.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x + graphics.trash2.width,
                                                                  graphics.trash2.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x,
                                                                  graphics.trash2.y + graphics.trash2.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash2.x + graphics.trash2.width,
                                                                  graphics.trash2.y + graphics.trash2.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:  # 代表四個角都不是paddle
                        break
                if paddle_checker:  # 代表四角有一角碰到paddle
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # 確認垃圾4有沒有撞上版
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x, graphics.trash4.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x + graphics.trash4.width,
                                                                  graphics.trash4.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x,
                                                                  graphics.trash4.y + graphics.trash4.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash4.x + graphics.trash4.width,
                                                                  graphics.trash4.y + graphics.trash4.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:  # 代表四個角都不是paddle
                        break
                if paddle_checker:  # 代表四角有一角碰到paddle
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # 確認trash7有沒有撞上板
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x, graphics.trash7.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x + graphics.trash7.width,
                                                                  graphics.trash7.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x,
                                                                  graphics.trash7.y + graphics.trash7.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash7.x + graphics.trash7.width,
                                                                  graphics.trash7.y + graphics.trash7.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:  # 代表四個角都不是paddle
                        break
                if paddle_checker:  # 代表四角有一角碰到paddle
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # 確認垃圾9有無撞上版
                paddle_checker = False
                while True:
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x, graphics.trash9.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x + graphics.trash9.width,
                                                                  graphics.trash9.y)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x,
                                                                  graphics.trash9.y + graphics.trash9.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    may_be_paddle = graphics.window.get_object_at(graphics.trash9.x + graphics.trash9.width,
                                                                  graphics.trash9.y + graphics.trash9.height)
                    if may_be_paddle is not None and may_be_paddle is graphics.paddle:
                        paddle_checker = True
                        break
                    if not paddle_checker:  # 代表四個角都不是paddle
                        break
                if paddle_checker:  # 代表四角有一角碰到paddle
                    graphics.switch = False
                    graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                        y=(graphics.window.height - graphics.ball.height) / 2)
                    number_of_attempts += 1  # 掛掉一次，等於玩一次
                    if number_of_attempts == 1:
                        graphics.live_label1.text = '❤️❤️'
                    elif number_of_attempts == 2:
                        graphics.live_label1.text = '❤️'
                    elif number_of_attempts == 3:
                        graphics.live_label1.text = ''
                    break

                # lv30以上出現黑洞
                if graphics.trash >= 30:
                    paddle_vx = random.randint(-10, 10)
                    graphics.paddle.move(paddle_vx, 0)
                    # 黑洞只會被貼上一次，故只有lv30時，開關會開可以貼上黑洞
                    if black_hole_add_switch:
                        graphics.window.add(graphics.black_hole_warning,
                                            x=(graphics.window.width-graphics.black_hole_warning.width)//2,
                                            y=(graphics.window.height-graphics.warning_asteroid_belt.height)//2+100)
                        graphics.window.add(graphics.black_hole_warning1,
                                            x=(graphics.window.width - graphics.black_hole_warning1.width) // 2,
                                            y=(graphics.window.height - graphics.warning_asteroid_belt.height)//2+150)
                        graphics.window.add(graphics.black_hole_1, x=(graphics.window.width-graphics.black_hole_1.width)/2,
                                            y=(graphics.window.height-graphics.black_hole_1.height)/2)
                        graphics.window.add(graphics.black_hole_2,
                                            x=(graphics.window.width - graphics.black_hole_1.width)/2+10,
                                            y=(graphics.window.height - graphics.black_hole_1.height)/2+10)
                        graphics.window.add(graphics.black_hole_3,
                                            x=(graphics.window.width - graphics.black_hole_1.width)/2+20,
                                            y=(graphics.window.height - graphics.black_hole_1.height)/2+20)
                        graphics.window.add(graphics.rock, x=80, y=200)
                        graphics.window.add(graphics.rock1, x=280, y=400)
                        graphics.window.add(graphics.rock2, x=400, y=180)
                        graphics.window.add(graphics.rock3, x=600, y=110)
                        graphics.window.add(graphics.rock4, x=550, y=270)
                        black_hole_add_switch = False
                    else:
                        graphics.black_hole_1.move(black_hole_vx, black_hole_vy)
                        graphics.black_hole_2.move(black_hole_vx, black_hole_vy)
                        graphics.black_hole_3.move(black_hole_vx, black_hole_vy)
                        graphics.rock.move(rock_vx, rock_vy)
                        graphics.rock1.move(rock_vx1, rock_vy1)
                        graphics.rock2.move(rock_vx2, rock_vy2)
                        graphics.rock3.move(rock_vx3, rock_vy3)
                        graphics.rock4.move(rock_vx4, rock_vy4)
                        if graphics.black_hole_1.x <= 0 or graphics.black_hole_1.x >= graphics.window.width:
                            black_hole_vx = -black_hole_vx
                        if graphics.black_hole_1.y <= 0 or graphics.black_hole_1.y >= graphics.window.height/2:
                            black_hole_vy = -black_hole_vy
                        if graphics.rock.x <= 0 or graphics.rock.x >= graphics.window.width:
                            rock_vx = -rock_vx
                        if graphics.rock1.x <= 0 or graphics.rock1.x >= graphics.window.width:
                            rock_vx1 = -rock_vx1
                        if graphics.rock2.x <= 0 or graphics.rock2.x >= graphics.window.width:
                            rock_vx2 = -rock_vx2
                        if graphics.rock3.x <= 0 or graphics.rock3.x >= graphics.window.width:
                            rock_vx3 = -rock_vx3
                        if graphics.rock4.x <= 0 or graphics.rock4.x >= graphics.window.width:
                            rock_vx4 = -rock_vx4
                        if graphics.rock.y <= 0 or graphics.rock.y+graphics.rock.height >= graphics.window.height:
                            rock_vy = -rock_vy
                        if graphics.rock1.y <= 0 or graphics.rock1.y+graphics.rock1.height >= graphics.window.height:
                            rock_vy1 = -rock_vy1
                        if graphics.rock2.y <= 0 or graphics.rock2.y+graphics.rock2.height >= graphics.window.height:
                            rock_vy2 = -rock_vy2
                        if graphics.rock3.y <= 0 or graphics.rock3.y+graphics.rock3.height >= graphics.window.height:
                            rock_vy3 = -rock_vy3
                        if graphics.rock4.y <= 0 or graphics.rock4.y+graphics.rock4.height >= graphics.window.height:
                            rock_vy4 = -rock_vy4
                # pause
                pause(FRAME_RATE)
        else:
            graphics.ball.move(0, 0)            # 當進入此圈，代表使用者未點按，故開關沒打開，vx和vy都是0，所以球看起來就像靜止的
        pause(FRAME_RATE)                       # 每圈都pause，才不會讓螢幕更新速度跟不上電腦運算速度而當機！！
        if number_of_attempts == NUM_LIVES:     # 三命用完，離開遊戲動畫回圈
            graphics.window.add(graphics.lose_bg, x=0, y=0)
            graphics.window.add(graphics.lose_img, x=(graphics.window.width - graphics.lose_img.width) // 2,
                                y=graphics.window.height - graphics.lose_img.height)
            break
        if number_of_brick_remove == num_of_bricks:
            graphics.window.add(graphics.win_bg, x=0, y=0)
            graphics.window.add(graphics.win_img, x=(graphics.window.width-graphics.win_img.width)//2,
                                y=graphics.window.height-graphics.win_img.height)
            break















if __name__ == '__main__':
    main()
