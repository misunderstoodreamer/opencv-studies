# python 05_basic_thresholding.py

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/coins01.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv.imread(args['image'])

# before apply thresholding ALWAYS make it grayscale and add a little bit blurring
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
blurred = cv.GaussianBlur(src=gray, ksize=(7, 7), sigmaX=0)
cv.imshow("Blurred", blurred)


# if pixel value is greater than our threshold (thresh=200 in this case),
# it is setted to be black, else it is white
(T, threshInv) = cv.threshold(src=blurred, thresh=200, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow("Threshold Binary Inv", threshInv)

# using normal thresholding
(T, thresh) = cv.threshold(src=blurred, thresh=200, maxval=255, type=cv.THRESH_BINARY)
cv.imshow("Threshold Binary", thresh)

# visualize only masked regions (helps later in ground truth implementation) -> bitwise ops.
masked = cv.bitwise_and(src1=image, src2=image, mask=threshInv)
cv.imshow("Output", masked)
cv.waitKey(0)

# Otsu Thresholding
(T, threshInv_otsu) = cv.threshold(src=blurred, thresh=200, maxval=255, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imshow("Threshold Otsu", threshInv_otsu)
print(f"Otsu Threshold value is {T}")

masked_otsu = cv.bitwise_and(src1=image, src2=image, mask=threshInv_otsu)
cv.imshow("Outsu Output", masked_otsu)
cv.waitKey(0)