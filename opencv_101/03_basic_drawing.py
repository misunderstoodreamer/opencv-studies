# python 04_basic_drawing.py
import random

# numpy is for creating empty canvas (in some sort of usage)
import numpy as np
import cv2 as cv

# initialize the canvas 300x300 pixel with rgb channels
canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw a green line from the top left corner of our canvas to the bottom right
green = 0, 255, 0  # bgr

cv.line(img=canvas, pt1=(0, 0), pt2=(300, 300), color=green)
cv.imshow(winname="Canvas", mat=canvas)
cv.waitKey(0)

# draw 3 px thick red start from top right to bottom left
red = 0, 0, 255
cv.line(img=canvas, pt1=(300, 0), pt2=(0, 300), color=red, thickness=3)
cv.imshow(winname="Canvas", mat=canvas)
cv.waitKey(0)

# draw green 50 px square, starts from 10, 10 ending at 60x60

cv.rectangle(img=canvas, pt1=(10, 10), pt2=(60, 60), color=green)
cv.imshow(winname='Canvas', mat=canvas)
cv.waitKey(0)

# draw another rectangle with thickness of 5 color is blue

blue = 255, 0, 0

cv.rectangle(img=canvas, pt1=(100, 100), pt2=(210, 210), color=blue, thickness=5)
cv.imshow(winname='Canvas', mat=canvas)
cv.waitKey(0)

# draw rectangle blue colored and filled

cv.rectangle(img=canvas, pt1=(40, 60), pt2=(110, 270), color=blue, thickness=-1)
cv.imshow(winname='Canvas', mat=canvas)
cv.waitKey(0)

# re-init the canvas draw dart table

white = 255, 255, 255

canvas = np.zeros(shape=(300, 300, 3), dtype="uint8")
center_x, center_y = canvas.shape[1] // 2, canvas.shape[0] // 2

for r in range(0, 175, 25):
    cv.circle(img=canvas, center=(center_x, center_y), radius=r, color=white)

cv.imshow("Canvas", canvas)
cv.waitKey(0)

# re-init the canvas and draw 25 random circles
canvas = np.zeros(shape=(300, 300, 3), dtype="uint8")

for i in range(0, 25):
    random_radius = np.random.randint(low=5, high=200)
    # always convert color to list. opencv may cause an error if you don't.
    # give me a int in range of 0, 255 and make it 3 times. then convert it to a list.
    random_color = np.random.randint(low=0, high=255, size=(3,)).tolist()
    # give me a int in range of 0, 300 and make it 2 times
    random_point = np.random.randint(low=0, high=300, size=(2,))
    cv.circle(img=canvas, center=random_point, radius=random_radius, color=random_color)

cv.imshow("Canvas", canvas)
cv.waitKey(0)