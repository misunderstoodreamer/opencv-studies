# python 02_morphological_ops_hats.py --image images/car.png

import argparse

import cv2
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
gray_scale = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)

# top (white) hat operation is used to reveal bright regions of an image on dark backgrounds
# black hat operation is used to reveal dark regions of an image on bright backgrounds
# construct a rect kernel (13,5)and apply blackhat operation which enables us to find dark regions on a light background
rect_kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=(13, 5))
blackhat = cv2.morphologyEx(src=gray_scale, op=cv.MORPH_BLACKHAT, kernel=rect_kernel)

# and then apply tophat (whitehat) operation will enable us to find bright regions on a dark background.
tophat = cv2.morphologyEx(src=gray_scale, op=cv.MORPH_TOPHAT, kernel=rect_kernel)

cv.imshow("Original Image", image)
cv.imshow("Blackhat Image", blackhat)
cv.imshow("Tophat Image", tophat)

cv.waitKey(0)

