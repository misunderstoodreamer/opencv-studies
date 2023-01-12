# python 07_cropping.py

import argparse
import cv2 as cv
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/bojack.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args['image'])
cv.imshow("Original", image)
cv.waitKey(0)

# [startY : endY, startX : endX]
# y = height-> number of rows
# x = width -> number of columns
head = image[50:335, 125:410]
cv.imshow("Bojack Head", head)
cv.waitKey(0)