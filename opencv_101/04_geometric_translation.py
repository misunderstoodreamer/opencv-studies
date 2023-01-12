import argparse
import cv2 as cv
import imutils
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/bojack.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args['image'])
cv.imshow("Original", image)

# shift the image 25 px to right and 50 px down

# define translate matrix M
"""
Translating image syntax:
    [
        [1, 0, shiftX],
        [0, 1, shiftY]
    ]
"""
M = np.float32([[1, 0, -25], [0, 1, 50]])
shifted = cv.warpAffine(src=image, M=M, dsize=(image.shape[1], image.shape[0]))
cv.imshow("Shifted Down and left", shifted)

# to make it simple, imutils lib will help.
shifted = imutils.translate(image=image, x=0, y=100)
cv.imshow("Shifted Down Only", shifted)

cv.waitKey(0)
