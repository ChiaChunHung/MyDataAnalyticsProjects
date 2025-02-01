# Coder
"""
This is a program that creates all of the object that
user needs in order to play the brick breaker game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constants 所有人皆可看到！
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=(self.window.height-paddle_offset))

        # Center a filled ball in the graphical window
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
            brick.fill_color = 'red'
            brick.color = 'red'
        elif i <= 3:
            brick.fill_color = 'gold'
            brick.color = 'gold'
        elif i <= 5:
            brick.fill_color = 'yellow'
            brick.color = 'yellow'
        elif i <= 7:
            brick.fill_color = 'green'
            brick.color = 'green'
        else:
            brick.fill_color = 'blue'
            brick.color = 'blue'

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

    def get_brick_num(self):
        return BRICK_COLS*BRICK_ROWS












