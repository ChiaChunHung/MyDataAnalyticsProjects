"""
File: mirror_lake.py
Name: Chia-Chun Hung
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: string, the filepath of mt-rainier.jpg.
    :return: SimpleImage, mt-rainier.jpg and its inverse version right below itself.
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            # 上半
            b_pixel_upper = b_img.get_pixel(x, y)
            b_pixel_upper.red = img_pixel.red
            b_pixel_upper.blue = img_pixel.blue
            b_pixel_upper.green = img_pixel.green
            # 下半
            b_pixel_lower = b_img.get_pixel(x, b_img.height-1-y)
            b_pixel_lower.red = img_pixel.red
            b_pixel_lower.blue = img_pixel.blue
            b_pixel_lower.green = img_pixel.green
    return b_img


def main():
    """
    This program will create a mirrored lake
    by placing an inverse image of mt-rainier.jpg
    below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
