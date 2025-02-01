"""
File: blur.py
Name: Chia-Chun Hung
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


# 寫法一
def blur(img):
    """
    :param img: SimpleImage, the image that is going to be blurred
    :return: SimpleImage, the blurry version of the original image
    """
    # create a new blank img that is as big as the original one
    b_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            # 先處裡四個角的Pixel模糊
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x+1, y)
                img_pixel_3 = img.get_pixel(x+1, y+1)
                img_pixel_4 = img.get_pixel(x, y + 1)
                green_avg = (img_pixel_1.green+img_pixel_2.green+img_pixel_3.green+img_pixel_4.green) // 4
                red_avg = (img_pixel_1.red+img_pixel_2.red+img_pixel_3.red+img_pixel_4.red) // 4
                blue_avg = (img_pixel_1.blue+img_pixel_2.blue+img_pixel_3.blue+img_pixel_4.blue) // 4
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x-1, y)
                img_pixel_3 = img.get_pixel(x-1, y+1)
                img_pixel_4 = img.get_pixel(x, y+1)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green) // 4
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red) // 4
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue) // 4
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x + 1, y)
                img_pixel_3 = img.get_pixel(x + 1, y - 1)
                img_pixel_4 = img.get_pixel(x, y - 1)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green) // 4
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red) // 4
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue) // 4
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x, y-1)
                img_pixel_3 = img.get_pixel(x-1, y)
                img_pixel_4 = img.get_pixel(x-1, y-1)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green) // 4
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red) // 4
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue) // 4
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            # 再處理位在四條邊上，但沒有同時位在四個角的Pixel模糊
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x-1, y)
                img_pixel_3 = img.get_pixel(x-1, y+1)
                img_pixel_4 = img.get_pixel(x, y+1)
                img_pixel_5 = img.get_pixel(x + 1, y + 1)
                img_pixel_6 = img.get_pixel(x+1, y)
                green_avg = (img_pixel_1.green+img_pixel_2.green+img_pixel_3.green+img_pixel_4.green+img_pixel_5.green+img_pixel_6.green)//6
                red_avg = (img_pixel_1.red+img_pixel_2.red+img_pixel_3.red+img_pixel_4.red+img_pixel_5.red +img_pixel_6.red)//6
                blue_avg = (img_pixel_1.blue+img_pixel_2.blue+img_pixel_3.blue+img_pixel_4.blue+img_pixel_5.blue+img_pixel_6.blue)//6
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x - 1, y)
                img_pixel_3 = img.get_pixel(x - 1, y - 1)
                img_pixel_4 = img.get_pixel(x, y - 1)
                img_pixel_5 = img.get_pixel(x + 1, y - 1)
                img_pixel_6 = img.get_pixel(x + 1, y)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green + img_pixel_6.green) // 6
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red + img_pixel_6.red) // 6
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue + img_pixel_6.blue) // 6
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x, y - 1)
                img_pixel_3 = img.get_pixel(x + 1, y - 1)
                img_pixel_4 = img.get_pixel(x + 1, y)
                img_pixel_5 = img.get_pixel(x + 1, y + 1)
                img_pixel_6 = img.get_pixel(x, y + 1)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green + img_pixel_6.green) // 6
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red + img_pixel_6.red) // 6
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue + img_pixel_6.blue) // 6
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                img_pixel_1 = img.get_pixel(x, y)
                img_pixel_2 = img.get_pixel(x, y - 1)
                img_pixel_3 = img.get_pixel(x - 1, y - 1)
                img_pixel_4 = img.get_pixel(x - 1, y)
                img_pixel_5 = img.get_pixel(x - 1, y + 1)
                img_pixel_6 = img.get_pixel(x, y + 1)
                green_avg = (img_pixel_1.green + img_pixel_2.green + img_pixel_3.green + img_pixel_4.green + img_pixel_5.green + img_pixel_6.green) // 6
                red_avg = (img_pixel_1.red + img_pixel_2.red + img_pixel_3.red + img_pixel_4.red + img_pixel_5.red + img_pixel_6.red) // 6
                blue_avg = (img_pixel_1.blue + img_pixel_2.blue + img_pixel_3.blue + img_pixel_4.blue + img_pixel_5.blue + img_pixel_6.blue) // 6
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
            # 最後處理中間部分
            else:
                # Inner pixels.
                pixel_1 = img.get_pixel(x-1, y-1)
                pixel_2 = img.get_pixel(x-1, y)
                pixel_3 = img.get_pixel(x - 1, y + 1)
                pixel_4 = img.get_pixel(x, y-1)
                pixel_5 = img.get_pixel(x, y)
                pixel_6 = img.get_pixel(x, y + 1)
                pixel_7 = img.get_pixel(x+1, y - 1)
                pixel_8 = img.get_pixel(x + 1, y)
                pixel_9 = img.get_pixel(x + 1, y + 1)
                green_avg = (pixel_1.green+pixel_2.green+pixel_3.green+pixel_4.green+pixel_5.green+pixel_6.green+pixel_7.green+pixel_8.green+pixel_9.green)//9
                red_avg = (pixel_1.red+pixel_2.red+pixel_3.red+pixel_4.red+pixel_5.red+pixel_6.red+pixel_7.red+pixel_8.red+pixel_9.red)//9
                blue_avg = (pixel_1.blue+pixel_2.blue+pixel_3.blue+pixel_4.blue+pixel_5.blue+pixel_6.blue+pixel_7.blue+pixel_8.blue+pixel_9.blue)//9
                b_pixel = b_img.get_pixel(x, y)
                b_pixel.red = red_avg
                b_pixel.blue = blue_avg
                b_pixel.green = green_avg
    return b_img


# 寫法二
def blur_2(img):
    b_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_sum = 0  # 等等裝附近所有格子的紅色數值的加總
            b_sum = 0  # 等等裝附近所有格子的藍色數值的加總
            g_sum = 0  # 等等裝附近所有格子的綠色數值的加總
            count = 0  # 計算周圍格子數目
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if 0 <= x+i < img.width and 0 <= y+j < img.height:
                        # 確保不會抓到座標之外的東西，
                        # 右邊不抓到x比0小的狀況，左邊不抓到超過寬長-1的狀況，設成寬長是因為上限不包
                        pixel = img.get_pixel(x+i, y+j)
                        # 抓出周圍所有的格子
                        r_sum += pixel.red
                        b_sum += pixel.blue
                        g_sum += pixel.green
                        count += 1
                        # 每進入此yes區間，就代表是一個附近的格子，所以分母數量加一
                        # 當是在邊界時，進入yes區間的次數就會變少，這反應了附近的格子變少
            b_pixel = b_img.get_pixel(x, y)
            # 取得新圖上同位置的Pixel
            b_pixel.red = r_sum // count
            # 該Pixel的紅色是原圖同位置pixel周圍和他自己的紅色數值的平均
            b_pixel.blue = b_sum // count
            # 該Pixel的藍色是原圖同位置pixel周圍和他自己的藍色數值的平均
            b_pixel.green = g_sum // count
            # 該Pixel的綠色是原圖同位置pixel周圍和他自己的綠色數值的平均
    return b_img


def main():
    """
    This program will blur the image the user give.
    """
    # 把圖檔以讀取圖檔的方式引入
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    # 把該圖檔丟到blur()去進行模糊
    blurred_img = blur(old_img)
    # 再把這張圖片用回圈模糊五次
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
