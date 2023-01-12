# python 06_resize.py

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

# resize image 150 wide and wide accordingly
ratio = 350 / image.shape[1]
dim = 350, int(image.shape[0] * ratio)

# performing resizing
resized = cv.resize(src=image, dsize=dim, interpolation=cv.INTER_AREA)
cv.imshow("Resized Focused Height", resized)
cv.waitKey(0)

# resize image 150 wide and wide accordingly
ratio = 250 / image.shape[0]
dim = int(image.shape[1] * ratio), 250

# performing resizing
resized = cv.resize(src=image, dsize=dim, interpolation=cv.INTER_AREA)
cv.imshow("Resized Focused Width", resized)
cv.waitKey(0)

# helper method imutils.resize

resized = imutils.resize(image=image, height=500)
cv.imshow("resized imultils", resized)
cv.waitKey(0)

# construct the list of interpolation methods in OpenCV
methods = [
    ("cv2.INTER_NEAREST", cv.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv.INTER_LINEAR),
    ("cv2.INTER_AREA", cv.INTER_AREA),
    ("cv2.INTER_CUBIC", cv.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv.INTER_LANCZOS4)]

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of the image by 2x using the current
    # interpolation method
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 2,
                             inter=method)
    cv.imshow("Method: {}".format(name), resized)
    cv.waitKey(0)
