# python 11_splitting_and_merging.py

import argparse
import cv2 as cv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/opencv_logo.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

# displaying each channel individually

B, G, R = cv.split(image)

cv.imshow("Red", R)
cv.imshow("Green", G)
cv.imshow("Blue", B)
cv.waitKey(0)

# then merging
merged = cv.merge([B, G, R])
cv.imshow("Merged", merged)
cv.waitKey(0)
cv.destroyAllWindows()
# visualize each channel in color

zeros = np.zeros(shape=image.shape[:2], dtype="uint8")
cv.imshow("Red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B, zeros, zeros]))
cv.waitKey(0)


