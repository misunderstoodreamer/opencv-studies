# python 09_bitwise_operations.py

import argparse
import cv2 as cv
import numpy as np

# draw a rectangle

rectangle = np.zeros(shape=(300, 300), dtype="uint8")
cv.rectangle(img=rectangle, pt1=(25, 25), pt2=(275, 275), color=255, thickness=-1)
cv.imshow("Rectangle", rectangle)

circle = np.zeros(shape=(300, 300), dtype="uint8")
center = circle.shape[1] // 2, circle.shape[0] // 2

cv.circle(img=circle, center=center, radius=(circle.shape[1] // 2) - 10, color=255, thickness=-1)
cv.imshow("Circle", circle)
cv.waitKey(0)


# Bitwise AND OR XOR

bitwise_and = cv.bitwise_and(src1=rectangle, src2=circle)
cv.imshow("BITWISE AND", bitwise_and)
cv.waitKey(0)

bitwise_or = cv.bitwise_or(src1=rectangle, src2=circle)
cv.imshow("BITWISE OR", bitwise_or)
cv.waitKey(0)

bitwise_xor = cv.bitwise_xor(src1=rectangle, src2=circle)
cv.imshow("BITWISE XOR", bitwise_xor)
cv.waitKey(0)

bitwise_not = cv.bitwise_not(src=circle)
cv.imshow("BITWISE NOT", bitwise_not)
cv.waitKey(0)
