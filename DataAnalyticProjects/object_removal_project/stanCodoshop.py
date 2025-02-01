"""
File: stanCodoshop.py
Name: Chia-Chun Hung
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
This program allows users to remove people from an image,
leaving only the beautiful background behind.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # calculation of the sum of RGB value of each pixel
    sum_of_red = 0
    sum_of_green = 0
    sum_of_blue = 0
    num_of_pixels = 0
    for pixel in pixels:
        sum_of_red += pixel.red
        sum_of_green += pixel.green
        sum_of_blue += pixel.blue
        num_of_pixels += 1
    # find the average of the RBG value of those pixels
    red = sum_of_red//num_of_pixels
    green = sum_of_green//num_of_pixels
    blue = sum_of_blue//num_of_pixels
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # avg_rgb_list == [red, green, blue]
    avg_rgb_list = get_average(pixels)

    # find the pixel with minimum distance from the avg point
    # because we need both the minimum distance and the pixel with that distance, we need to use the concept of bundle

    # first data processing
    min_dist = get_pixel_dist(pixels[0], avg_rgb_list[0], avg_rgb_list[1], avg_rgb_list[2])
    min_pixel = pixels[0]

    # second and after data
    for i in range(1, len(pixels)):
        dist_of_candidate = get_pixel_dist(pixels[i], avg_rgb_list[0], avg_rgb_list[1], avg_rgb_list[2])
        if dist_of_candidate < min_dist:
            min_dist = dist_of_candidate
            min_pixel = pixels[i]
    return min_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # Write code to populate image and create the 'ghost' effect
    for i in range(images[0].height):
        for j in range(images[0].width):
            pixels = []
            for image in images:
                pixels.append(image.get_pixel(j, i))
            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(j, i)
            result_pixel.red = best_pixel.red
            result_pixel.blue = best_pixel.blue
            result_pixel.green = best_pixel.green
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
