"""
File: my_drawing.py
Name: Tony
----------------------
This program uses several Classes in the GObject
to create many geometric objects, in order to draw
a naughty dog.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Naughty dog

    It is a naughty dog, because it took me
    three days to draw, but I still love it,
    since it gave me a great sense of accomplishment,
    once I completed creating it.
    """
    # canvas
    window = GWindow(800, 800)

    # Background
    bg = GRect(800, 800)
    bg.filled = True
    bg.fill_color = 'oldlace'

    # face
    face = GPolygon()
    face.add_vertex((150, 285))
    face.add_vertex((150, 385))
    face.add_vertex((350, 530))
    face.add_vertex((450, 530))
    face.add_vertex((650, 385))
    face.add_vertex((650, 285))
    face.filled = True
    face.fill_color = 'lightgoldenrodyellow'
    face.color = 'lightgoldenrodyellow'

    # eyebrow（含眉心）
    # 眉心上
    eyebrow = GRect(100, 50, x=350, y=233)
    eyebrow.filled = True
    eyebrow.fill_color = 'saddlebrown'
    eyebrow.color = 'saddlebrown'
    # 眉心下
    eyebrow_1 = GRect(100, 50, x=350, y=284)
    eyebrow_1.filled = True
    eyebrow_1.fill_color = 'goldenrod'
    eyebrow_1.color = 'goldenrod'
    # 左眉
    eyebrow_2 = GRect(89, 50, x=260, y=234)
    eyebrow_2.filled = True
    eyebrow_2.fill_color = 'ivory'
    eyebrow_2.color = 'ivory'
    # 右眉
    eyebrow_3 = GRect(89, 50, x=451, y=234)
    eyebrow_3.filled = True
    eyebrow_3.fill_color = 'ivory'
    eyebrow_3.color = 'ivory'

    # eye
    # left eye
    left_eye = GPolygon()
    left_eye.add_vertex((260, 284))
    left_eye.add_vertex((289, 256))
    left_eye.add_vertex((323, 256))
    left_eye.add_vertex((349, 284))
    left_eye.add_vertex((349, 313))
    left_eye.add_vertex((328, 335))
    left_eye.add_vertex((279, 335))
    left_eye.add_vertex((260, 313))
    left_eye.filled = True
    left_eye_center = GOval(35, 35, x=289, y=270)
    left_eye_center.filled = True
    left_eye_center.fill_color = 'white'
    # right eye
    right_eye = GPolygon()
    right_eye.add_vertex((449, 284))
    right_eye.add_vertex((478, 256))
    right_eye.add_vertex((512, 256))
    right_eye.add_vertex((538, 284))
    right_eye.add_vertex((538, 313))
    right_eye.add_vertex((517, 335))
    right_eye.add_vertex((468, 335))
    right_eye.add_vertex((449, 313))
    right_eye.filled = True
    right_eye_center = GOval(35, 35, x=478, y=270)
    right_eye_center.filled = True
    right_eye_center.fill_color = 'white'

    # upper head（額頭）
    # 中間最長的方塊
    upper_head = GRect(100, 110, x=350, y=123)
    upper_head.filled = True
    upper_head.fill_color = 'saddlebrown'
    upper_head.color = 'saddlebrown'
    # 左邊梯形
    left_upper_head = GPolygon()
    left_upper_head.add_vertex((260, 233))
    left_upper_head.add_vertex((349, 233))
    left_upper_head.add_vertex((349, 123))
    left_upper_head.add_vertex((329, 123))
    left_upper_head.add_vertex((260, 185))
    left_upper_head.filled = True
    left_upper_head.fill_color = 'goldenrod'
    left_upper_head.color = 'goldenrod'
    # 左邊三角形
    left_upper_tri = GPolygon()
    left_upper_tri.add_vertex((260, 185))
    left_upper_tri.add_vertex((260, 284))
    left_upper_tri.add_vertex((150, 284))
    left_upper_tri.filled = True
    left_upper_tri.fill_color = 'darkgoldenrod'
    left_upper_tri.color = 'darkgoldenrod'
    # 右邊梯形
    right_upper_head = GPolygon()
    right_upper_head.add_vertex((450, 233))
    right_upper_head.add_vertex((541, 233))
    right_upper_head.add_vertex((541, 185))
    right_upper_head.add_vertex((470, 123))
    right_upper_head.add_vertex((450, 123))
    right_upper_head.filled = True
    right_upper_head.fill_color = 'goldenrod'
    right_upper_head.color = 'goldenrod'
    # 右邊三角形
    right_upper_tri = GPolygon()
    right_upper_tri.add_vertex((541, 185))
    right_upper_tri.add_vertex((541, 284))
    right_upper_tri.add_vertex((651, 284))
    right_upper_tri.filled = True
    right_upper_tri.fill_color = 'darkgoldenrod'
    right_upper_tri.color = 'darkgoldenrod'

    # mouse
    # 整個底
    mouse = GPolygon()
    mouse.add_vertex((350, 334))
    mouse.add_vertex((260, 384))
    mouse.add_vertex((260, 464))
    mouse.add_vertex((350, 530))
    mouse.add_vertex((450, 530))
    mouse.add_vertex((541, 464))
    mouse.add_vertex((541, 384))
    mouse.add_vertex((449, 334))
    mouse.filled = True
    mouse.fill_color = 'tan'
    mouse.color = 'tan'
    # 底的上半部
    mouse_2 = GPolygon()
    mouse_2.add_vertex((350, 334))
    mouse_2.add_vertex((260, 384))
    mouse_2.add_vertex((260, 424))
    mouse_2.add_vertex((325, 466))
    mouse_2.add_vertex((478, 466))
    mouse_2.add_vertex((541, 424))
    mouse_2.add_vertex((541, 384))
    mouse_2.add_vertex((449, 334))
    mouse_2.filled = True
    mouse_2.fill_color = 'lightgoldenrodyellow'
    mouse_2.color = 'lightgoldenrodyellow'
    # 下巴
    mouse_3 = GPolygon()
    mouse_3.add_vertex((319, 470))
    mouse_3.add_vertex((319, 485))
    mouse_3.add_vertex((365, 530))
    mouse_3.add_vertex((450, 530))
    mouse_3.add_vertex((491, 500))
    mouse_3.add_vertex((491, 470))
    mouse_3.filled = True
    mouse_3.fill_color = 'saddlebrown'
    mouse_3.color = 'saddlebrown'
    # 下嘴唇
    mouse_4 = GPolygon()
    mouse_4.add_vertex((329, 470))
    mouse_4.add_vertex((489, 470))
    mouse_4.add_vertex((469, 490))
    mouse_4.add_vertex((339, 490))
    mouse_4.filled = True
    mouse_4.fill_color = 'lightgoldenrodyellow'
    mouse_4.color = 'lightgoldenrodyellow'

    # chin (命名錯，但真的懶得改，其實這是牙齒的部分)
    chin = GRect(160, 25, x=319, y=445)
    chin.filled = True

    # nose
    nose = GRect(100, 40, x=350, y=359)
    nose.filled = True
    nose_shadow = GRect(74, 25, x=350, y=359)
    nose_shadow.filled = True
    nose_shadow.fill_color = 'dimgray'
    nose_bottom = GRect(70, 12, x=363, y=399)
    nose_bottom.filled = True
    nose_oval = GArc(63, 56, 270, 90, x=418, y=383)
    nose_oval.filled = True
    nose_oval_2 = GArc(63, 56, 180, 90, x=350, y=383)
    nose_oval_2.filled = True

    # chick
    # 左臉頰
    chick = GRect(30, 40, x=260, y=384)
    chick.filled = True
    # 左臉頰上方三角形
    chick_1 = GPolygon()
    chick_1.add_vertex((260, 384))
    chick_1.add_vertex((290, 384))
    chick_1.add_vertex((290, 365))
    chick_1.filled = True
    chick_1.fill_color = 'tan'
    chick_1.color = 'tan'
    # 左臉頰下方扇形
    chick_2 = GArc(120, 65, 180, 90, x=260, y=405)
    chick_2.filled = True
    # 左臉頰下方牙齒
    chick_4 = GPolygon()
    chick_4.add_vertex((290, 430))
    chick_4.add_vertex((290, 444))
    chick_4.add_vertex((300, 444))
    chick_4.filled = True
    # 左牙齒下方扇形
    chick_5 = GArc(110, 100, 180, 90, x=290, y=420)
    chick_5.filled = True

    # 右臉頰
    chick_r = GRect(30, 40, x=511, y=384)
    chick_r.filled = True
    # 右臉頰上方三角形
    chick_r1 = GPolygon()
    chick_r1.add_vertex((511, 384))
    chick_r1.add_vertex((541, 384))
    chick_r1.add_vertex((511, 365))
    chick_r1.filled = True
    chick_r1.fill_color = 'tan'
    chick_r1.color = 'tan'
    # 右臉頰下方扇形
    chick_r2 = GArc(120, 65, 270, 90, x=481, y=405)
    chick_r2.filled = True
    # 右臉頰下方牙齒
    chick_r4 = GPolygon()
    chick_r4.add_vertex((510, 430))
    chick_r4.add_vertex((510, 444))
    chick_r4.add_vertex((500, 444))
    chick_r4.filled = True
    # 右牙齒下方扇形
    chick_r5 = GArc(117, 100, 270, 90, x=451, y=420)
    chick_r5.filled = True

    # 最外圈：最左和右側臉頰、脖子
    # 最左臉頰
    lefest_chick = GPolygon()
    lefest_chick.add_vertex((150, 285))
    lefest_chick.add_vertex((115, 310))
    lefest_chick.add_vertex((115, 400))
    lefest_chick.add_vertex((150, 440))
    lefest_chick.filled = True
    lefest_chick.fill_color = 'goldenrod'
    lefest_chick.color = 'goldenrod'
    # 最右臉頰
    rightest_chick = GPolygon()
    rightest_chick.add_vertex((651, 285))
    rightest_chick.add_vertex((686, 310))
    rightest_chick.add_vertex((686, 400))
    rightest_chick.add_vertex((651, 440))
    rightest_chick.filled = True
    rightest_chick.fill_color = 'peru'
    rightest_chick.color = 'peru'

    # 脖子
    # 左側
    neck = GPolygon()
    neck.add_vertex((150, 385))
    neck.add_vertex((150, 440))
    neck.add_vertex((350, 585))
    neck.add_vertex((350, 530))
    neck.filled = True
    neck.fill_color = 'tan'
    neck.color = 'tan'
    # 中間方塊
    neck_1 = GRect(100, 55, x=350, y=530)
    neck_1.filled = True
    neck_1.fill_color = 'tan'
    neck_1.color = "tan"

    neck_2 = GRect(50, 23, x=400, y=530)
    neck_2.filled = True
    neck_2.fill_color = 'lightgoldenrodyellow'
    neck_2.color = 'lightgoldenrodyellow'

    neck_4 = GRect(50, 33, x=350, y=552)
    neck_4.filled = True
    neck_4.fill_color = 'beige'
    neck_4.color = 'beige'
    # 右側
    neck_5 = GPolygon()
    neck_5.add_vertex((450, 530))
    neck_5.add_vertex((450, 585))
    neck_5.add_vertex((651, 440))
    neck_5.add_vertex((651, 385))
    neck_5.filled = True
    neck_5.fill_color = 'tan'
    neck_5.color = 'tan'

    # 脖子下方的身體
    body = GPolygon()
    body.add_vertex((260, 521))
    body.add_vertex((260, 585))
    body.add_vertex((350, 585))
    body.filled = True
    body.fill_color = 'lightgoldenrodyellow'
    body.color = 'lightgoldenrodyellow'
    body_1 = GPolygon()
    body_1.add_vertex((260, 521))
    body_1.add_vertex((260, 585))
    body_1.add_vertex((240, 585))
    body_1.add_vertex((150, 521))
    body_1.add_vertex((150, 440))
    body_1.filled = True
    body_1.fill_color = 'goldenrod'
    body_1.color = 'goldenrod'
    body_2 = GPolygon()
    body_2.add_vertex((150, 440))
    body_2.add_vertex((150, 470))
    body_2.add_vertex((220, 521))
    body_2.add_vertex((258, 521))
    body_2.filled = True
    body_2.fill_color = 'saddlebrown'
    body_2.color = 'saddlebrown'
    # 脖子下方右側身體
    body_3 = GPolygon()
    body_3.add_vertex((450, 585))
    body_3.add_vertex((571, 585))
    body_3.add_vertex((651, 521))
    body_3.add_vertex((651, 440))
    body_3.filled = True
    body_3.fill_color = 'saddlebrown'
    body_3.color = 'saddlebrown'

    body_4 = GPolygon()
    body_4.add_vertex((450, 585))
    body_4.add_vertex((541, 585))
    body_4.add_vertex((541, 520))
    body_4.filled = True
    body_4.fill_color = 'peru'
    body_4.color = 'peru'

    # ear
    # left ear
    ear = GPolygon()
    ear.add_vertex((150, 285))
    ear.add_vertex((150, 93))
    ear.add_vertex((200, 50))
    ear.add_vertex((239, 52))
    ear.add_vertex((329, 123))
    ear.filled = True
    ear.fill_color = 'goldenrod'
    ear.color = 'goldenrod'
    # left ear content
    ear_1 = GPolygon()
    ear_1.add_vertex((260, 70))
    ear_1.add_vertex((260, 185))
    ear_1.add_vertex((329, 123))
    ear_1.filled = True
    ear_1.fill_color = 'saddlebrown'
    ear_1.color = 'saddlebrown'

    ear_2 = GPolygon()
    ear_2.add_vertex((200, 80))
    ear_2.add_vertex((200, 243))
    ear_2.add_vertex((260, 186))
    ear_2.add_vertex((260, 80))
    ear_2.filled = True

    ear_3 = GPolygon()
    ear_3.add_vertex((200, 78))
    ear_3.add_vertex((200, 103))
    ear_3.add_vertex((230, 103))
    ear_3.add_vertex((230, 123))
    ear_3.add_vertex((260, 123))
    ear_3.add_vertex((260, 78))
    ear_3.filled = True
    ear_3.fill_color = 'white'
    ear_3.color = 'white'

    # right ear
    ear_r1 = GPolygon()
    ear_r1.add_vertex((469, 123))
    ear_r1.add_vertex((579, 52))
    ear_r1.add_vertex((618, 50))
    ear_r1.add_vertex((651, 93))
    ear_r1.add_vertex((651, 284))
    ear_r1.filled = True
    ear_r1.fill_color = 'goldenrod'
    ear_r1.color = 'goldenrod'
    # right ear content
    ear_r2 = GPolygon()
    ear_r2.add_vertex((469, 123))
    ear_r2.add_vertex((541, 77))
    ear_r2.add_vertex((541, 188))
    ear_r2.filled = True
    ear_r2.fill_color = 'saddlebrown'
    ear_r2.color = 'saddlebrown'

    ear_r3 = GPolygon()
    ear_r3.add_vertex((542, 76))
    ear_r3.add_vertex((542, 187))
    ear_r3.add_vertex((601, 243))
    ear_r3.add_vertex((601, 76))
    ear_r3.filled = True

    ear_r4 = GPolygon()
    ear_r4.add_vertex((542, 76))
    ear_r4.add_vertex((542, 121))
    ear_r4.add_vertex((572, 121))
    ear_r4.add_vertex((572, 101))
    ear_r4.add_vertex((601, 101))
    ear_r4.add_vertex((601, 76))
    ear_r4.filled = True
    ear_r4.fill_color = 'white'
    ear_r4.color = 'white'

    # Label
    label = GLabel('I am a bad dog,', x=100, y=640)
    label_1 = GLabel('Because, I took my owner 3 days to create.', x=100, y=670)
    label.font = '-30-bold'
    label_1.font = '-30-bold'


    # add to canvas
    window.add(bg)
    window.add(face)
    window.add(eyebrow)
    window.add(eyebrow_1)
    window.add(eyebrow_2)
    window.add(eyebrow_3)
    window.add(left_eye)
    window.add(left_eye_center)
    window.add(right_eye)
    window.add(right_eye_center)
    window.add(upper_head)
    window.add(left_upper_head)
    window.add(left_upper_tri)
    window.add(right_upper_head)
    window.add(right_upper_tri)
    window.add(mouse)
    window.add(mouse_2)
    window.add(nose)
    window.add(nose_shadow)
    window.add(nose_bottom)
    window.add(nose_oval)
    window.add(nose_oval_2)
    window.add(chick)
    window.add(chick_1)
    window.add(chick_2)
    window.add(chick_4)
    window.add(chick_5)
    window.add(chin)
    window.add(chick_r)
    window.add(chick_r1)
    window.add(chick_r2)
    window.add(chick_r4)
    window.add(chick_r5)
    window.add(lefest_chick)
    window.add(rightest_chick)
    window.add(neck)
    window.add(neck_1)
    window.add(neck_2)
    window.add(neck_4)
    window.add(neck_5)
    window.add(mouse_3)
    window.add(mouse_4)
    window.add(ear)
    window.add(ear_1)
    window.add(ear_2)
    window.add(ear_3)
    window.add(ear_r1)
    window.add(ear_r2)
    window.add(ear_r3)
    window.add(ear_r4)
    window.add(body)
    window.add(body_1)
    window.add(body_2)
    window.add(body_3)
    window.add(body_4)
    window.add(label)
    window.add(label_1)


if __name__ == '__main__':
    main()
