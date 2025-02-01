"""
File: draw_line.py
Name: Tony
-------------------------
When the user click the mouse odd number of times,
this program will draw a circle , and, when the user
click the mouse even number of times, draw a line
starting at the point where the user click the mouse last time
, then removing the circle.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant controls the radius of the circle
SIZE = 5

# Global variables
window = GWindow()  # 做出canvas
times_of_click = 0  # 點按次數，用於判斷奇偶
odd_clicks_x = 0    # 奇數次點擊時的滑鼠位置資訊
odd_clicks_y = 0    # 奇數次點擊時的滑鼠位置資訊


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(drawing_process)


def drawing_process(mouse):
    """
    This function defines the actions that the computer
    should undertake every time the user clicked the mouse.
    """
    global times_of_click                                       # 告知電腦此變數是全域變數而非常數，這樣才能對他做Reassign
    times_of_click += 1                                         # 當使用者按一次滑鼠，就在裝點擊次數的變數箱中加一次
    if times_of_click % 2 != 0:                                 # 若為奇數次點擊
        draw_a_circle(mouse.x, mouse.y)                         # 則畫圈
    else:                                                       # 若為偶數次點擊
        draw_a_line(mouse.x, mouse.y)                           # 則把兩點連線並消除起點的圈


def draw_a_circle(mouse_x, mouse_y):                            # 此Function會畫圈並記錄下起點位置
    """
    :param: mouse_x, int, x coordinate of user's mouse
    :param: mouse_y, int, y coordinate of user's mouse
    """
    global odd_clicks_x
    global odd_clicks_y
    oval = GOval(SIZE*2, SIZE*2)
    window.add(oval, x=mouse_x-SIZE, y=mouse_y-SIZE)
    odd_clicks_x = mouse_x                                      # 記錄奇數次點擊時，滑鼠的x座標
    odd_clicks_y = mouse_y                                      # 記錄奇數次點擊時，滑鼠的y座標


def draw_a_line(mouse_x, mouse_y):                              # 此Function會畫線並移除奇數次點擊時生成的圈
    """
    :param: mouse_x, int, x coordinate of user's mouse
    :param: mouse_y, int, y coordinate of user's mouse
    """
    # 起點和終點連線
    line = GLine(odd_clicks_x, odd_clicks_y, mouse_x, mouse_y)
    window.add(line)
    # 消掉奇數次點擊所生成的圈
    odd_clicks_circle = window.get_object_at(odd_clicks_x-SIZE/2, odd_clicks_y-SIZE/2)
    # 若是抓奇數次點擊以滑鼠為中心做的圓的左上角的基準點的位置，那會抓不到物件，因為正方形內接圓的半徑比正方形的對角線除2還要短，
    # 但若抓滑鼠起點座標的位置，會連同線本身一起抓到，變成把線消掉，
    # 所以只好在起點圓的圓心往左邊走該圓半徑的一半，往上走該圓半徑的一半的位置去抓，這樣就一定會抓到圓的裡面，且不會去抓到線。
    window.remove(odd_clicks_circle)



if __name__ == "__main__":
    main()
