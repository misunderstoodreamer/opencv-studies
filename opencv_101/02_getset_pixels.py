# python .\02_getset_pixels.py -i .\images\hey_small.jpg

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the input image")
args = vars(ap.parse_args())

# load the image and take the height and width
# image = cv.imread(r"images/hey_small.jpg")
image = cv.imread(args['image'])

# **every numpy array has .shape attribute**
# height = number of rows, width = number of columns
h, w = image.shape[:2]
cv.imshow("Original Image", image)


# because of the images are just an array, we can extract values at specific point of the image

def access_pixels(height, width):
    b, g, r = image[width, height]
    print(f"Pixels at ({height}, {width}): Red - {r}, Green - {g}, Blue - {b}".format(r, g, b))


def update_pixels(height, width):
    image[width, height] = 0, 0, 255  # set to red
    b, g, r = image[width, height]
    print(f"Pixels at ({height}, {width}): Red - {r}, Green - {g}, Blue - {b}".format(r, g, b))


access_pixels(0, 0)
access_pixels(100, 150)
update_pixels(100, 150)

cX, cY = w // 2, h // 2

tl = image[0:cY, 0:cX]
# cv.imshow("tl", tl)

tr = image[0:cY, cX:w]
# cv.imshow("tr", tr)

bl = image[cY:h, 0:cX]
# cv.imshow("bl", bl)

br = image[cY:h, cX:w]
# cv.imshow("br", br)


image[0:cY, 0:cX] = 0, 255, 0

cv.imshow("Green Top Left", image)
cv.waitKey(0)
