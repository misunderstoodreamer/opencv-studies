# python 11_auto_edge_detection.py

import argparse
import cv2 as cv
import numpy as np


def auto_canny(image, sigma=0.33):
    # computing the median of the single channel pixel intensities
    v = np.median(image)

    # applying automatic Canny edge detection using computed median value
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv.Canny(image=image, threshold1=lower, threshold2=upper)

    return edged


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=r".\images\dolphin.png",
                help="path to the input image")
args = vars(ap.parse_args())

# load image and make it gray scale to perform operations
image = cv.imread(args['image'])
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(src=gray, ksize=(3, 3), sigmaX=0)

wide = cv.Canny(image=blurred, threshold1=10, threshold2=200)
tight = cv.Canny(image=blurred, threshold1=240, threshold2=250)
auto = auto_canny(image=blurred)

cv.imshow("Original", image)
cv.imshow("Edges Wide - Tight - Auto", np.hstack([wide, tight, auto]))
cv.waitKey(0)
