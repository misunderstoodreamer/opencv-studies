# python 09_magnitude_orientation.py

import argparse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=r".\images\coins02.png",
                help="path to the input image")

args = vars(ap.parse_args())

# load image and make it gray scale to perform operations

image = cv.imread(args['image'])
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

# computing gradients along with x_axis and y_axis

gX = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)
gY = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)

# compute the gradient maginitude and orientation
magnitude = np.sqrt((gX ** 2), (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# combine the gradient representations into single image
combined = cv.addWeighted(src1=gX, alpha=0.5, src2=gY, beta=0.5, gamma=0)

# figure displaying

(fig, axs) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
axs[0].imshow(gray, cmap="gray")
axs[1].imshow(magnitude, cmap="jet")
axs[2].imshow(orientation, cmap="jet")

axs[0].set_title("grayscale")
axs[1].set_title("gradient orientation")
axs[2].set_title("gradient orientation [0, 180]")

for i in range(0, 3):
    axs[i].get_xaxis().set_ticks([])
    axs[i].get_yaxis().set_ticks([])

plt.tight_layout()
plt.show()
