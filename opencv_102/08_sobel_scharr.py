# python 08_sobel_scharr.py

import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/bricks.png",
                help="path to the input image")
ap.add_argument("-s", "--scharr", type=int, default=0,
                help="path to the input image")
args = vars(ap.parse_args())

# load image and make it gray scale to perform operations

image = cv.imread(args['image'])
gray = cv.cvtColor(src=image, code=cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

# whatever operator you using (sobel or scharr), first set the kernel size.
# then compute gradients along with the x and y axis respectively

ksize = -1 if args["scharr"] > 0 else 3
gX = cv.Sobel(src=gray, ddepth=cv.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv.Sobel(src=gray, ddepth=cv.CV_32F, dx=0, dy=1, ksize=ksize)

# gradient magnitude images are now of floating point data type, so we need to take care to convert them
# back to unsigned 8-bit integer representation so other opencv functions can operate them and visulaize them.

gX = cv.convertScaleAbs(src=gX)
gY = cv.convertScaleAbs(src=gY)

# combine the gradient representations into single image
combined = cv.addWeighted(src1=gX, alpha=0.5, src2=gY, beta=0.5, gamma=0)

# displaying
cv.imshow("Sobel/Scharr X", gX)
cv.imshow("Sobel/Scharr Y", gY)
cv.imshow("Sobel/Scharr Combined", combined)
cv.waitKey(0)
