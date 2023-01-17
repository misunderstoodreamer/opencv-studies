# python 10_edge_detection.py

import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=r".\images\coins02.png",
                help="path to the input image")

args = vars(ap.parse_args())

# load image and make it gray scale to perform operations

image = cv.imread(args['image'])
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

cv.imshow("Original", gray)
cv.imshow("Blurred", blurred)

# apply canny edge detection wide, mid-range, tight
# before not know knowing what is wide, mid-range, tight,
# https://pyimagesearch.com/2021/05/12/opencv-edge-detection-cv2-canny/
# read this article

wide = cv.Canny(image=blurred, threshold1=10, threshold2=200)
mid_range = cv.Canny(image=blurred, threshold1=30, threshold2=150)
tight = cv.Canny(image=blurred, threshold1=240, threshold2=250)

cv.imshow("Wide Edge Map", wide)
cv.imshow("Mid Edge Map", mid_range)
cv.imshow("Tight Edge Map", tight)
cv.waitKey(0)
