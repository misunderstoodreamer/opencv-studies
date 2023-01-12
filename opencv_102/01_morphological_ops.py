# python 01_morphological_ops.py --image images/pyimagesearch_logo.png

import argparse

import cv2
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path of the input image")
args = vars(ap.parse_args())

# loading the image then convert to the grayscale, and display the image

image = cv.imread(args["image"])

# if you do morphological ops, turn it to grayscale first.
gray_scaled = cv.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
# thresholding, adaptive treshholding, edge detection.. BINARY
cv.imshow(winname="gray image", mat=gray_scaled)
cv.waitKey(0)

# applying erosions
for i in range(0, 3):
    eroded = cv.erode(src=gray_scaled.copy(), kernel=None, iterations=i + 1)
    cv.imshow(winname="Eroded {} times".format(i + 1), mat=eroded)
    cv.waitKey(0)

cv.destroyAllWindows()
cv.imshow("Original Image", image)

# applying dilations
for i in range(0, 3):
    dilate = cv.dilate(src=gray_scaled.copy(), kernel=None, iterations=i + 1)
    cv.imshow(winname="Dilated {} times".format(i + 1), mat=dilate)
    cv.waitKey(0)
cv.destroyAllWindows()

kernel_sizes = [(3, 3), (5, 5), (7, 7)]
# constructing a rect kernel from the current size and then apply an "opening" operation
for kernel_size in kernel_sizes:
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=kernel_size)
    opening = cv.morphologyEx(src=gray_scaled, op=cv.MORPH_OPEN, kernel=kernel)
    cv.imshow("Opening: ({}, {})".format(kernel_size[0], kernel_size[1]), opening)
    cv.waitKey(0)

cv.destroyAllWindows()
cv.imshow("Original Image", image)

# constructing a rect kernel from the current size but this time apply a "closing" operation
for kernel_size in kernel_sizes:
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=kernel_size)
    closing = cv.morphologyEx(src=gray_scaled, op=cv.MORPH_CLOSE, kernel=kernel)
    cv.imshow("Closing: ({}, {})".format(kernel_size[0], kernel_size[1]), closing)
    cv.waitKey(0)

cv.destroyAllWindows()
cv.imshow("Original Image", image)

# morphological gradient
# outline or boundary detection

for kernel_size in kernel_sizes:
    kernel = cv.getStructuringElement(shape=cv.MORPH_RECT, ksize=kernel_size)
    gradient = cv.morphologyEx(src=gray_scaled, op=cv.MORPH_GRADIENT, kernel=kernel)
    cv.imshow("Gradient: ({}, {})".format(kernel_size[0], kernel_size[1]), gradient)
    cv.waitKey(0)


