# python 03_blurring.py --image images/hey_small.jpg

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)
# in convolutions kernel sizes must be odd, large kernel size -> more pixel that computer computing
kernel_sizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernel_sizes:
    # applying basic average blur
    blurred = cv.blur(src=image, ksize=(kX, kY))
    cv.imshow("Average ({}, {})".format(kX, kY), mat=blurred)
    cv.waitKey(0)

cv.destroyAllWindows()
# cv.imshow("Original Image", image)

for (kX, kY) in kernel_sizes:
    # applying gaussian blur
    blurred = cv.GaussianBlur(src=image, ksize=(kX, kY), sigmaX=0)
    cv.imshow("Gaussian Blur ({}, {})".format(kX, kY), mat=blurred)
    cv.waitKey(0)

cv.destroyAllWindows()
cv.imshow("Original Image", image)

for k in (3, 9, 15):
    # applying median blur
    blurred = cv.medianBlur(src=image, ksize=k)
    cv.imshow("Median Blur {}".format(k), mat=blurred)
    cv.waitKey(0)

# bilateral filtering
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for (diameter, sigma_color, sigma_space) in params:
    # apply bilateral filtering to the image using current set of parameters
    bilateral_blurred = cv.bilateralFilter(src=image, d=diameter,
                                           sigmaColor=sigma_color,
                                           sigmaSpace=sigma_space)
    cv.imshow("Bilateral Blur d={}, sc={}, ss={}".format(diameter, sigma_color, sigma_space), bilateral_blurred)
    cv.waitKey(0)
