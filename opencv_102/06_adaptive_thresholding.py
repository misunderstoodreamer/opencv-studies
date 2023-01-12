# python 06_adaptive_thresholding.py

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/steve_jobs.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args['image'])

# before apply thresholding ALWAYS make it grayscale and add a little bit blurring
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
blurred = cv.GaussianBlur(src=gray, ksize=(7, 7), sigmaX=0)
cv.imshow("Blurred", blurred)

# Simple Thresholding
(Th, threshInv) = cv.threshold(src=blurred, thresh=200, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholding", threshInv)

# Otsu Thresholding
(T, threshInv_otsu) = cv.threshold(src=blurred, thresh=200, maxval=255, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imshow("Threshold Otsu", threshInv_otsu)
print(f"Otsu Threshold value is {T}")

cv.waitKey(0)

# average blurring considers entire region underneath the kernel
adaptive_thresh_mean = cv.adaptiveThreshold(src=blurred, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,
                                       thresholdType=cv.THRESH_BINARY_INV, blockSize=21, C=10)
cv.imshow("adaptive trash mean", adaptive_thresh_mean)
cv.waitKey(0)

adaptive_thresh_gaussian = cv.adaptiveThreshold(src=blurred, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       thresholdType=cv.THRESH_BINARY_INV, blockSize=21, C=4)
cv.imshow("adaptive trash gaussian", adaptive_thresh_gaussian)
cv.waitKey(0)
