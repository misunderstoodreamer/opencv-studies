# python 04_color_spaces.py

import argparse
import cv2 as cv

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, default="images/hey_small.jpg",
#                 help="path to the input image")
# args = vars(ap.parse_args())
#
# image = cv.imread(args['image'])

path = r'images/hey_small.jpg'
image = cv.imread(path)
cv.imshow("Original RGB", image)

for (name, chan) in zip(("B", "G", "R"), cv.split(image)):
    cv.imshow(name, chan)

cv.waitKey(0)
cv.destroyAllWindows()

# HSV
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)
for (name, chan) in zip(("H", "S", "V"), cv.split(hsv)):
    cv.imshow(name, chan)

cv.waitKey(0)
cv.destroyAllWindows()

# L*a*b*
lab = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("l*a*b*", lab)

for (name, chan) in zip(("L*", "a*", "b*"), cv.split(lab)):
    cv.imshow(name, chan)

cv.waitKey(0)
cv.destroyAllWindows()

# grayscale
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
cv.imshow("original", image)
cv.imshow("gray", gray)

cv.waitKey(0)
