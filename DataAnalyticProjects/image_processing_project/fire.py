"""
File: fire.py
Name: Chia-Chun Hung
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""

from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: string, the filepath of the image that is going to be analyzed
    :return: SimpleImage, the image that shows where the fire was
    """
    highlight_fire_img = SimpleImage(filename)
    for pixel in highlight_fire_img:
        avg = (pixel.red + pixel.blue + pixel.green)//3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return highlight_fire_img


def main():
    """
    This program detects the pixels that are recognized as fire
    and highlights them for better observation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
