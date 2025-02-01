# Coder
"""
This is a program that creates all of the object that
user needs in order to play a brick breaker game with
more levels and enhanced content!!
"""

from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random


# Constants 所有人皆可看到！
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 20        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window_width = window_width
        self.window_height = window_height

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-paddle_offset))

        # Center a ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.animate_of_paddle)                                      # 先做讓paddle跟著滑鼠中心移動的code
        onmouseclicked(self.game_start_ball_drop)                                 # 使用者點按，球獲得速度
        self.switch = False                                                       # 使用者點擊前，球獲得速度的開關皆是關閉的

        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_offset = brick_offset
        self.brick_spacing = brick_spacing
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.draw_bricks()                                                       # 呼叫絕招來畫出所有磚塊

        # 存Scene要用的變數
        # start scene background color
        self.start_scene_bg = GRect(self.window_width, self.window_height)
        self.start_scene_bg.filled = True
        # start scene earth
        self.earth = GImage('earth.png')
        # start scene story
        self.story_line0 = GLabel('Space cleaning crew !')
        self.story_line0.color = 'Gold'
        self.story_line0.font = '-30-Bold'
        self.story_line1 = GLabel('In search of a new home,')
        self.story_line1.color = 'white'
        self.story_line2 = GLabel('Humanity has launched a pioneer exploration spacecraft.')
        self.story_line2.color = 'white'
        self.story_line3 = GLabel('The spacecraft ventures into the uncharted expanse of outer space')
        self.story_line3.color = 'white'
        self.story_line4 = GLabel('However, the ship encounters an asteroid belt')
        self.story_line4.color = 'white'
        self.story_line5 = GLabel('As the pilot aboard,')
        self.story_line5.color = 'white'
        self.story_line6 = GLabel('you must maneuver an energy ball to clear the obstacles ahead')
        self.story_line6.color = 'white'
        self.story_line7 = GLabel(', paving a safe path for the migration fleet that follows.')
        self.story_line7.color = 'white'
        self.click_to_start = GLabel('Click to start!')
        self.click_to_start.color = 'Gold'
        self.click_to_start.font = '-30-Bold'
        self.start_warning = GLabel('Please do not click until the animation ends!!')
        self.start_warning.color = 'red'
        self.start_warning.font = '-15-Bold'

        # 製作幾分版
        self.trash = 0
        self.trash_collect = GLabel('Trash You Collect ' + str(self.trash))
        self.trash_collect.font = '-20-Bold'

        # 製作幾命
        self.live_label1 = GLabel('❤️❤️❤️')
        self.live_label1.font = '-25'

        # 製作太空垃圾事件出現前的動畫
        self.event_scene = GRect(self.window_width, self.window_height)
        self.event_scene.filled = True
        self.event_scene2 = GRect(self.window_width, self.window_height)
        self.event_scene2.filled = True
        self.event_scene2.fill_color = 'red'
        self.warning_asteroid_belt = GLabel('Warning! An Asteroid Belt is coming!')
        self.warning_asteroid_belt.font = '-40-Bold'
        self.warning_asteroid_belt.color = 'red'

        # 製作太空垃圾
        self.trash1 = GRect(40, 40)
        self.trash1.filled = True
        self.trash1.fill_color = 'silver'

        self.trash2 = GRect(35, 35)
        self.trash2.filled = True
        self.trash2.fill_color = 'red'

        self.trash3 = GOval(40, 40)
        self.trash3.filled = True
        self.trash3.fill_color = 'silver'

        self.trash4 = GRect(35, 35)
        self.trash4.filled = True
        self.trash4.fill_color = 'red'

        self.trash5 = GRect(50, 50)
        self.trash5.filled = True
        self.trash5.fill_color = 'silver'

        self.trash6 = GRect(25, 25)
        self.trash6.filled = True
        self.trash6.fill_color = 'silver'

        self.trash7 = GRect(40, 40)
        self.trash7.filled = True
        self.trash7.fill_color = 'red'

        self.trash8 = GOval(50, 50)
        self.trash8.filled = True
        self.trash8.fill_color = 'silver'

        self.trash9 = GRect(40, 40)
        self.trash9.filled = True
        self.trash9.fill_color = 'red'

        # 製作黑洞
        self.black_hole_1 = GOval(150, 150)
        self.black_hole_1.filled = True
        self.black_hole_1.fill_color = 'dimgray'
        self.black_hole_2 = GOval(100, 100)
        self.black_hole_2.filled = True
        self.black_hole_2.fill_color = 'lightgray'
        self.black_hole_3 = GOval(70, 70)
        self.black_hole_3.filled = True
        self.black_hole_3.fill_color = 'black'
        self.black_hole_warning = GLabel('Warning! You Encounter a Black Hole!')
        self.black_hole_warning.color = 'red'
        self.black_hole_warning.font = '-30-Bold'
        self.black_hole_warning1 = GLabel('The strong Gravity field will influence your control!')
        self.black_hole_warning1.color = 'red'
        self.black_hole_warning1.font = '-30-Bold'

        # rock pull by black hole
        self.rock = GOval(40, 40)
        self.rock1 = GOval(45, 45)
        self.rock2 = GOval(55, 55)
        self.rock3 = GOval(35, 35)
        self.rock4 = GOval(30, 30)
        self.rock.filled = True
        self.rock1.filled = True
        self.rock2.filled = True
        self.rock3.filled = True
        self.rock4.filled = True

        # Win img
        self.win_img = GImage('doggy2.png')
        self.win_bg = GRect(self.window.width, self.window.height)
        self.win_bg.filled = True
        self.win_bg.fill_color = 'oldlace'

        # lose img
        self.lose_img = GImage('lose2.png')
        self.lose_bg = GRect(self.window.width, self.window.height)
        self.lose_bg.filled = True
        self.lose_bg.fill_color = 'oldlace'

        # 畫出磚塊
    def draw_bricks(self):
        brick_construction_x = 0                                                 # 用來存放每個磚塊的x座標
        brick_construction_y = self.brick_offset                                 # 用來存放每個磚塊的y座標
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                brick = GRect(self.brick_width, self.brick_height)
                self.brick_color_painting(i, brick)                              # 此絕招因為沒有用用到物件，所以Class也可做
                self.window.add(brick, x=brick_construction_x, y=brick_construction_y)
                brick_construction_x += (self.brick_width + self.brick_spacing)  # 讓磚塊的x座標可以向右移
            brick_construction_x = 0                                             # 當換一列時，磚塊的x座標可以重新從0開始
            brick_construction_y += (self.brick_height + self.brick_spacing)     # 讓磚塊的y座標可以向下移

    @staticmethod
    def brick_color_painting(i, brick):
        brick.filled = True
        if i <= 1:
            brick.fill_color = 'black'
            brick.color = 'black'
        elif i <= 3:
            brick.fill_color = 'dimgray'
            brick.color = 'dimgray'
        elif i <= 5:
            brick.fill_color = 'gray'
            brick.color = 'gray'
        elif i <= 7:
            brick.fill_color = 'slategray'
            brick.color = 'slategray'
        else:
            brick.fill_color = 'lightgray'
            brick.color = 'lightgray'

    def animate_of_paddle(self, mouse):  # 每當滑鼠移動，paddle的中心要跟著滑鼠移動且當paddle碰到邊界，paddle不可超出邊界
        if mouse.x-self.paddle.width/2 <= 0:
            self.window.add(self.paddle, x=0, y=self.paddle.y)
        elif mouse.x+self.paddle.width/2 >= self.window.width:
            self.window.add(self.paddle, x=self.window.width-self.paddle.width, y=self.paddle.y)
        else:
            self.window.add(self.paddle, x=mouse.x-(self.paddle.width/2), y=self.paddle.y)

    def game_start_ball_drop(self, mouse):
        self.switch = True                          # 使用者點按後，球獲得速度的開關被打開
        # 給球隨機初速
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter：
    # 分享球的初速給使用者
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    @staticmethod
    def get_brick_num():
        return BRICK_COLS*BRICK_ROWS











