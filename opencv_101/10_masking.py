# python 10_masking.py

import argparse
import cv2 as cv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/bojack.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

# a general mask is same size as your image, but has only 2 pixel values (0 for background, 255 for mask)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv.rectangle(img=mask, pt1=(125, 50), pt2=(410, 335), color=255, thickness=-1)
cv.imshow("Rectangular Mask", mask)
cv.waitKey(0)

# apply mask to image
masked = cv.bitwise_and(src1=image, src2=image, mask=mask)
cv.imshow("Mask Applied", masked)
cv.waitKey(0)

# create a circlar mask with radius of 100

circular_mask = np.zeros(image.shape[:2], dtype="uint8")
cv.circle(img=circular_mask, center=(300, 200), thickness=-1, radius=100, color=255)
masked = cv.mask(src1=image, src2=image, mask=circular_mask)
cv.imshow("Circle Mask Applied", masked)
cv.waitKey(0)
